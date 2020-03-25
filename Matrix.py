import random
import math
class Matrix():
	def __init__(self,num_rows,num_cols):
		self.rows = num_rows
		self.cols = num_cols
		self.data = []
		for i in range(self.rows):
			self.data.append([])
			for j in range(self.cols):
				self.data[i].append(0)

	def randomize(self): 
		for i in range(self.rows):
			for j in range(self.cols):
				self.data[i][j] = random.uniform(-1,1)

	@staticmethod 
	def subtract(a,b):
		result = Matrix(a.rows, b.cols)
		for i in range(result.rows):
			for j in range(result.cols):
				result.data[i][j] = a.data[i][j] - b.data[i][j]
		return result

	def plus(self, x): 
		if (type(x)==Matrix):
			for i in range(self.rows):
				for j in range(self.cols):
					self.data[i][j] += x.data[i][j]
		else:
			for i in range(self.rows):
				for j in range(self.cols):
					self.data[i][j] += x
	@staticmethod
	def transpose(mat):
		result = Matrix(mat.cols, mat.rows)
		for i in range(mat.rows):
			for j in range(mat.cols):
				result.data[j][i] += mat.data[i][j]
		return result

	@staticmethod 
	def multiply(n,m):
		if (type(m)==Matrix):
				result = Matrix(n.rows, m.cols)
				for i in range(result.rows):
					for j in range(result.cols):
						sum = 0
						for k in range(n.cols):
							sum += n.data[i][k] * m.data[k][j]
						result.data[i][j] = sum;
				return result

	def scaler(self,n):
		if (type(n) !=Matrix):
			for i in range(self.rows):
				for j in range(self.cols):
					self.data[i][j] *= n
			
	@staticmethod
	def toArray(mat):
		output_arr = []
		for i in range(mat.rows):
			for j in range(mat.cols):
				output_arr.append(mat.data[i][j])
		return output_arr
		
	@staticmethod
	def toMatrix(arr): 
		mat = Matrix(len(arr), 1)
		for i in range(len(arr)):
			mat.data[i][0] = arr[i]
		return mat 

	@staticmethod 
	def sigmoid(x):
		for i in range(x.rows):
			for j in range(x.cols):
				val = x.data[i][j]
				x.data[i][j] = 1 / ( 1 + math.exp(-val));
		return x

	@staticmethod
	def disgmoid(y): 
		for i in range(y.rows):
			for j in range(y.cols):
				val = y.data[i][j]
				y.data[i][j] = val * ( 1 - val)
		return y
