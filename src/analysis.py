"""Original synthetic segmentation and purchase-propensity analysis."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
rng=np.random.default_rng(19); n=5000
D=pd.DataFrame({"age":rng.integers(18,75,n),"income":rng.lognormal(10.7,.5,n),"loyalty_months":rng.integers(0,96,n),"annual_spend":rng.gamma(3,420,n),"email_engagement":rng.beta(2.2,4,n)})
z=-4.1+.000018*D.income+.012*D.loyalty_months+.00055*D.annual_spend+1.7*D.email_engagement
D["organic_buyer"]=rng.binomial(1,1/(1+np.exp(-z)))
X=((D.iloc[:,:5]-D.iloc[:,:5].mean())/D.iloc[:,:5].std()).to_numpy(); k=4; C=X[rng.choice(n,k,False)]
for _ in range(40):
 lab=((X[:,None,:]-C[None,:,:])**2).sum(2).argmin(1); new=np.array([X[lab==j].mean(0) for j in range(k)])
 if np.allclose(new,C): break
 C=new
D["segment"]=lab
S=D.groupby("segment").agg(customers=("age","size"),buyer_rate=("organic_buyer","mean"),avg_spend=("annual_spend","mean"),avg_loyalty=("loyalty_months","mean")).round(2)
print(S)
out=Path(__file__).parents[1]/"assets"; out.mkdir(exist_ok=True)
fig,ax=plt.subplots(1,2,figsize=(10,4.5)); S.buyer_rate.plot.bar(ax=ax[0],color="#16a085",title="Organic buyer rate by segment"); ax[0].set_ylabel("Rate"); S.avg_spend.plot.bar(ax=ax[1],color="#f59e0b",title="Average annual spend"); ax[1].set_ylabel("Synthetic dollars"); fig.suptitle("Synthetic customer segments"); fig.tight_layout(); fig.savefig(out/"segment-summary.png",dpi=180); plt.close(fig)
