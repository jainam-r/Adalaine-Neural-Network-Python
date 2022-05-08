x1 = [1,1,-1,-1]
x2 = [1,-1,1,-1]
print("0. AND\n1. OR\n2. XOR\n3. NOR\n4. NAND")
gate_type = int(input("Input the type of gate: "))
if gate_type == 0:
    t = [1,-1,-1,-1]
elif gate_type == 1:
    t = [1,1,1,-1]
elif gate_type == 2:
    t = [-1,1,1,-1]
elif gate_type == 3:
    t = [-1,-1,-1,1]
elif gate_type == 4:
    t = [-1,1,1,1]
else:
    print("Input invalid")
print(f"""
x1   x2   t
{x1[0]}   {x2[0]}   {t[0]}
{x1[1]}   {x2[1]}   {t[1]}
{x1[2]}   {x2[2]}   {t[2]}
{x1[3]}   {x2[3]}   {t[3]}
""")
ep = int(input("Enter number of epochs you want to train the model for: "))
class Adaline(object):
    def __init__(self,epochs,x1,x2,t,lr=0.1,weights=[0.1,0.1],bias=0.1):
        self.epochs = epochs
        self.lr = lr
        self.weights = weights
        self.bias = bias
        self.x1 = x1
        self.x2 = x2
        self.t = t
    def y_in(self,n_iter):
        self.y = round(self.bias + (self.weights[0]*self.x1[n_iter]) + (self.weights[1]*self.x2[n_iter]),2)
        return self.y
    def update_weights(self,n_iter):
        self.weights = [round(self.weights[0]+(self.lr*(self.t[n_iter]-self.y)*self.x1[n_iter]),2),round(self.weights[1]+
                                                                    (self.lr*(self.t[n_iter]-self.y)*self.x2[n_iter]),2)]
        return self.weights
    def update_bias(self,n_iter):
        self.bias = round(self.bias + (self.lr*(self.t[n_iter]-self.y)),2)
        return self.bias
    def error(self,n_iter):
        error = (self.t[n_iter]-self.y)**2
        return error
    def fit(self):
        for i in range(self.epochs):
            print(f"Epoch = {i+1}")
            tot_err = 0
            for ter in range(4):
                print(f"  Iteration : {ter}")
                print(f"     Weights in iteration {ter}: [{self.weights[0]},{self.weights[1]}]")
                self.y_in(ter)
                print(f"     Output y is: {self.y}")
                self.update_weights(ter)
                self.update_bias(ter)
                print(f"     Bias is: {self.bias}")
                er = self.error(ter)
                print(f"     Error = {round(er,2)}")
                tot_err = tot_err + er
            print(f"Epoch{i+1} error = {round(tot_err,3)}")

#Onlyc change the first parameter which is the number of epochs
ada = Adaline(ep,x1,x2,t) 
ada.fit()