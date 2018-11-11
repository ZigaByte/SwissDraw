class Swiss:
	def __init__(self, A, d, n):
		self.A = A
		self.d = d
		
		self.m = len(d) # Number of matches
		self.n = n # Number of teams

	# Gradient descent
	def descentStep(self, A, s, d, alpha):
		for k in range(self.n):
			s[k] = s[k] - alpha * sum([(sum([A[i][j]*s[j] for j in range(self.n)]) - d[i]) * A[i][k] for i in range(self.m)]) 
		return s

	# Find a group containing the team i
	def findGroup(self, A, i):	
		group = []
		group.append(i)
		
		increased = True
		while(increased):
			increased = False
			for j in group:
				for i in range(len(A)):
					if(A[i][j] != 0):
						# Find the element from that row
						for k in range(len(A[i])):
							if(k != j and A[i][k] != 0):
								if(not(k in group)):
									increased = True
									group.append(k)
		return group

	# Find all the groups
	def findGroups(self, A, s):
		groups = []
		inAGroup = [False] * self.n
		
		while (not all(v == True for v in inAGroup)):
			for i in range(len(inAGroup)):
				if(not inAGroup[i]):
					groups.append(self.findGroup(A, i))
					for new in groups[-1]:
						inAGroup[new] = True
		return groups
			
	# Normalize the scores of teams. (sum(Abs[s[i] for i in group])) has to be 0
	def normalizeScores(self, A, s):
		groups = self.findGroups(A, s)
		print(groups)
		
		for group in groups:
			scoreSum = 0
			for team in group:
				scoreSum += s[team]
			for team in group:
				s[team] -= scoreSum / len(group)
		
		return s
	
	# Round the scores to 3 decimals 
	def roundScores(self, s):
		decimals = 3
		s = [round(si * 10**(decimals)) / 10**(decimals) for si in s]
		return s
	
	# Run the score calculation
	def getScores(self):
		alpha = 0.1
		
		s = [0] * self.n
		delta = 100
		while delta > 1e-7:
			ns = self.descentStep(self.A, s.copy(), self.d, alpha\)
			delta = max([abs(nsi - si) for si, nsi in zip(s, ns)])
			s = ns
			
		s = self.normalizeScores(self.A, s)
		print(s)
		s = self.roundScores(s)
		print(s)
		
		return s

