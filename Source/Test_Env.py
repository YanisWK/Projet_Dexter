from Source.Environnement import * 

Env1 = Environnement(1,10,10)
print(Env1)
HEnv1=Env1.getH()
LEnv1=Env1.getL()
print(HEnv1,LEnv1)
Env1.setHandL(6,6)
HEnv1=Env1.getH()
LEnv1=Env1.getL()
print(HEnv1,LEnv1)
