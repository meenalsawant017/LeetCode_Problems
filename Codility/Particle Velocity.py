'''

Link:- https://algo.monster/problems/particle_velocity

You are a programmer in a scientific team doing research into particles. As an experiment, you have measured the position of a single particle in N equally distributed moments of time. The measurement made in moment K is recorded in an array particles as particles[K].

Now, your job is to count all the periods of time when the movement of the particle was stable. Those are the periods during which the particle doesn't change its velocity: i.e. the difference between any two consecutive position measurements remains the same. Note that you need at least three measurements to be sure that the particle didn't change its velocity.

For Example
1, 3, 5, 7, 9 is stable (velocity is 2)
7, 7, 7, 7 is stable (particle stays in place)
3, -1, -5, -9 is stable (velocity is 4)
0, 1 is not stable (you need at least three measurements)
1, 1, 2, 5, 7 is not stable (velocity changes between measurements)


Example:
Input: [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
Output: 5
Explanation:
Possible periods of time for which velocity is stable are:

values	location(from, to)	Velocity
[-1, 1, 3]	(0,2)	2
[3, 3, 3]	(2,4)	0
[3, 2, 1, 0]	(6,9)	-1
[3, 2, 1]	(6,8)	-1
[2, 1, 0]	(7,9)	-1


Example 1:
Input: [1, 3, 5, 7, 9]
Output: 6
Explanation:
Possible periods of time for which velocity is stable are:

values	location(from, to)	Velocity
[1, 3, 5]	(0,2)	2
[3, 5, 7]	(1,3)	2
[5, 7, 9]	(2,4)	2
[1, 3, 5, 7, 9]	(0,4)	2
[1, 3, 5, 7]	(0,3)	2
[3, 5, 7, 9]	(1,4)	2

'''

'''def particleVelocity(particles):
      i = 0
      j = 1
      velocity = 0
      
      while i < len(particles)- 2:
            while j < len(particles) - 1:
                  sliding_window = j - i + 1
                  prev_velocity = particles[j] -  particles[i]
                  print( 'i', i,'j',j,'prev_velocity', prev_velocity, 'sliding_window', sliding_window)
                  if sliding_window != 3:
                        if j < len(particles) - 1:
                              j +=1
                        else:
                              print('else')
                              return velocity
                        curr_velocity = particles[j] -  particles[i+1]
                        print('i', i,'j',j,'curr_velocity',curr_velocity)
                        if curr_velocity == prev_velocity:
                              velocity += abs(prev_velocity)
                              print('match-->', velocity)
                  i += 1
            
      return velocity
      '''
def particleVelocity(particles):
    print(len(particles))
    numStable = 0
    if len(particles) < 3:
       return 0
    for i in range(len(particles) - 2):
        for j in range(i + 1, len(particles) - 1):
            print('i', i, 'particles[i]', particles[i], 'j:', j, 'particles[j]', particles[j])
            print('j diff:', particles[j + 1] - particles[j], 'i diff',particles[i + 1] - particles[i])
            if particles[j + 1] - particles[j] == particles[i + 1] - particles[i]:
                numStable += 1
                print('i', i,'j',j)
            else :
                break
    return numStable if numStable < 1000000000 else -1


particles=  [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]#[7, 7, 7, 7]#[1, 3, 5, 7, 9]
res = particleVelocity(particles)
print(res)
