class palyer:

    Ban_most_Run = 0

    def __init__(self , run) -> None:
        self.run = run

    def hit_four(self):
        self.run += 4
        palyer.Ban_most_Run +=4

    def hit_six(self):
        self.run += 6
        palyer.Ban_most_Run +=6

    def sengel_run(self):
        self.run +=1
        palyer.Ban_most_Run +=1
    


#=====================================================================================================

#print(palyer.Ban_most_Run)
Tamim = palyer(0)
Liton_Das = palyer(0)
Tamim.hit_four()
Tamim.sengel_run()
Liton_Das.hit_four()
Tamim.sengel_run()
Liton_Das.hit_four()
Liton_Das.hit_six()
Liton_Das.sengel_run()
Tamim.hit_six()
#palyer.Ban_most_Run()
print("Ban = ",palyer.Ban_most_Run)
print("Tamim Run: " ,Tamim.run)
print("Liton_Das Run :" ,Liton_Das.run)


