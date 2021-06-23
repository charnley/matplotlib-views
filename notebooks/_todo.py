

# Get hist in log-scale
n_bins = 5
hist, bins = np.histogram(outliers_removed, bins=n_bins)
logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
#plt.hist(x, bins=logbins)
#plt.xscale('log')

n, bins, patches = ax.hist(
    outliers_removed,
    #bins=logbins,
    histtype='stepfilled', color="k", density=False
)
#ax.set_xscale("log")
#ax.set_yscale("log")

views.fix_borders(ax)
ax.set_ylabel("Count")
ax.set_xlabel("Desc [unit]")
