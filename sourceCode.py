'''

Algorithm : Retinex-Based Fast Algorithm for Low-Light Image 
			Enhancement 

Language : Python 3.9 

Used Technology : OpenCv

Used Library : OpenCv2

'''

#importing Required Libraries
import cv2
import math 


class RBFAlgorithm:

	#Constructor With Parameter Image path
	def __init__(self,imgpath):
		#open img and store it in class member using cv2.imread() method 
		self.inputImage=cv2.imread(imgpath,1)
		#store the Dimensions of the image
		self.Rows,self.Columns,self.useless=self.inputImage.shape
		#converting BGR Color image to grayScale image 
		self.grayImg=cv2.cvtColor(self.inputImage,cv2.COLOR_BGR2GRAY)
		#converting BGR color Image to HSV Image
		self.hsvImg=cv2.cvtColor(self.inputImage,cv2.COLOR_BGR2HSV)
		#copy the V channel of HSV for further use
		self.vChannel=self.hsvImg[:,:,2].copy()
		#copy the S Channel of HSV  for further use 
		self.sChannel=self.hsvImg[:,:,1].copy()
		#stores the output Image 
		self.outputImage=None

		self.enhancedVChannelImg=None
		self.enhancedSChannelImg=None
		#to count the frequencies of different pixel Values of V channel and S channel of HSV image
		self.grayFreq=[0 for i in range(256)]
		self.sGrayFreq=[0 for i in range(256)]
		'''
			calculating the frequencies of each pixel in two channels 

		'''
		for i in range(self.Rows):
			for j in range(self.Columns):
				self.grayFreq[self.grayImg[i][j]]+=1
				self.sGrayFreq[self.sChannel[i][j]]+=1


	#To get the maximum Gray level Value from V channel of HSV Image
	def getVmax(self):
		maxValue=0
		for i in range(self.Rows):
			for j in range(self.Columns):
				maxValue=max(maxValue,self.vChannel[i][j])
		return maxValue

	#to get the maximum Gray level value from S channel of HSV Image
	def getSmax(self):
		maxValue=0
		for i in range(Rows):
			for j in range(Columns):
				maxValue=max(ans,self.sChannel[i][j])
		return maxValue

	#to Get the frequency of  V channel PixelValue
	def getFrequency(self,pixelValue):
		return self.grayFreq[pixelValue]

	#to Get the frequency of S channel pixel Value
	def getSFrequency(self,pixelValue):
		return self.sGrayFreq[pixelValue]



	#Mean Gray Value
	def getMeanGrayValue(self):
		temp1=0
		temp2=0
		for pixelValue in range(256):
			pixelFreq=self.getFrequency(pixelValue)
			temp1+=(pixelFreq*pixelValue)
			temp2+=(pixelFreq)
		mean=temp1//temp2
		return mean


	#to get constant value
	def getConstant(self):
		mean=self.getMeanGrayValue()
		temp1=0
		temp2=0
		for pixelValue in range(0,mean+1):
			temp1+=(self.getFrequency(pixelValue)*pixelValue)
			temp2+=(self.getFrequency(pixelValue))

		temp2=128*temp2
		constantVal=temp1/temp2
		return constantVal


	def getEnlargedConstant(self):
		constantVal=self.getConstant()
		return (1//(1+math.pow(math.e,-constantVal)))



	def getPDF(self,pixelValue):
		ans=self.getFrequency(pixelValue)
		ans=ans/(self.Rows*self.Columns)
		return ans



	def getCDF(self):
		final_cdf=0
		for pixelValue in range(0,129):
			final_cdf+=(self.getPDF(pixelValue))

		print("cdfvalue : ",final_cdf)
		return final_cdf



	def getGamma(self):
		c1=self.getEnlargedConstant()
		cdf=self.getCDF()
		w=0.48
		ansGamma=w*(c1)+(1-w)*cdf
		return ansGamma



	def applyVChannelEnhancing(self):
		vmaxValue=self.getVmax()
		self.enhancedVChannelImg=self.hsvImg[:,:,2].copy()
		gamma=self.getGamma()
		for i in range(self.Rows):
			for j in range(self.Columns):
				self.enhancedVChannelImg[i][j]=((255//vmaxValue)*self.enhancedVChannelImg[i][j])

		for i in range(self.Rows):
			for j in range(self.Columns):
				oldvalue=self.enhancedVChannelImg[i][j]
				oldvalue=oldvalue/255
				temp=math.pow(oldvalue,gamma)
				temp=int(temp*255)
				self.enhancedVChannelImg[i][j]=temp


		temp111=self.enhancedVChannelImg.copy()
		temp222=self.hsvImg[:,:,2].copy()


		for i in range(self.Rows):
			for j in range(self.Columns):
				change1=temp111[i][j]/255
				change2=temp222[i][j]/255
				if change1!=0:
					change1=math.log(change1)
				if change2!=0:
					change2=math.log(change2)
				if(change1!=0):
					self.enhancedVChannelImg[i][j]=int(255*math.pow(math.e,(change2-change1)))

		self.applyDynamicExpansion()


	#Dynamic Range Expansion
	def applyDynamicExpansion(self):
		for i in range(self.Rows):
			for j in range(self.Columns):
				temp1=self.enhancedVChannelImg[i][j]

				if(self.enhancedVChannelImg[i][j]<100):
					temp1=temp1/255
					temp1=2.5*math.pow(temp1,2)
					temp1=temp1*255
					self.enhancedVChannelImg[i][j]=int(temp1)

		


	def getVE_Mean(self):
		ve_freq=[0 for i in range(256)]
		for i in range(self.Rows):
			for j in range(self.Columns):
				ve_freq[self.enhancedVChannelImg[i][j]]+=1
		ve_mean=0
		for pixelValue in range(256):
			ve_mean+=(ve_freq[pixelValue]*pixelValue)
		ve_mean=ve_mean/(self.Rows*self.Columns)
		return ve_mean




	def getSMean(self):
		smean=0
		for pixelValue in range(256):
			smean+=(self.sGrayFreq[pixelValue]*pixelValue)
		smean=smean/(self.Rows*self.Columns)
		return smean


	def getVES(self):
		ve_mean=self.getVE_Mean()
		smean=self.getSMean()
		return ve_mean-smean

	def applySChannelEnhancing(self):
		n=0
		ves=self.getVES()
		if ves>=0:
			n=1

		self.enhancedSChannelImg=self.sChannel.copy()
		for i in range(self.Rows):
			for j in range(self.Columns):
				tempvalue=self.sChannel[i][j]/255
				ves=ves/255
				tempPow=1+math.pow(-1,2-n)*(math.pow(abs(ves),2)+abs(ves))
				tempvalue=math.pow(tempvalue,tempPow)
				tempvalue=int(tempvalue*255)
				self.enhancedSChannelImg[i][j]=tempvalue
		


	def showoutput(self):
		cv2.imshow("output",self.outputImage)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


	def Enhance(self):
		self.applyVChannelEnhancing()
		self.applySChannelEnhancing()
		self.hsvImg[:,:,2]=self.enhancedVChannelImg
		self.hsvImg[:,:,1]=self.enhancedSChannelImg
		self.outputImage=cv2.cvtColor(self.hsvImg,cv2.COLOR_HSV2BGR)


	def saveOutput(self,outputName):
		cv2.imwrite(outputName,self.outputImage)
		


obj1=RBFAlgorithm('input1.jpg')
obj1.Enhance()
obj1.saveOutput('output1.jpg')


obj2=RBFAlgorithm('input2.jpg')
obj2.Enhance()
obj2.saveOutput('output2.jpg')

obj3=RBFAlgorithm('input3.jpg')
obj3.Enhance()
#obj1.showoutput()
obj3.saveOutput('output3.jpg')
