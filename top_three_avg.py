Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def top_three_avg(g1,g2,g3,g4):
	"""(number,number,number,number)->float
         return the average of the top three of grades:

         >>>top_thre_avg(90,80,70,60)
         80
         """
	total=g1+g2+g3+g4
	top_three=total-min(g1,g2,g3,g4)
	return float(top_three/3)
