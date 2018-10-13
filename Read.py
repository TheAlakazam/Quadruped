
# this function is in a class just because 
# all other functions are in classes
# uniformity you know ;P

class Read:
	@staticmethod
	def read_from_file(filename,th1=0,th2=0,th3=0):
		motion_set=[]
		try:
			file=open(filename,'r')
			angles=file.read()

			motions=angles.split('\n')
			motions=filter(None,motions)
			
			for motion in motions:
				motion_split=motion.split('|')
				r_ang_str,r_wait_time = motion_split[0],motion_split[1]
				ang_str=str(r_ang_str).strip()
				wait_time=str(r_wait_time).strip()
				ang_list_str=ang_str.split()
				ang_list_float=[float(x) for x in ang_list_str]

				motion_set.append([ang_list_float,float(wait_time)])
			
		except IOError:
			raise "File not found\n"

		return filter(None,motion_set)

