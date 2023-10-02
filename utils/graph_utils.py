from config import *
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc


def visualize_cor_matrix(fig_path, train_data):
    """Visualize correlation matrix"""
    sns.set(style="white")
    corr_matrix = train_data.corr().abs()
    mask = np.zeros_like(corr_matrix, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(1, 2, figsize=(20, 10))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(train_data.corr(), cmap=cmap, ax=ax[0])
    sns.heatmap(corr_matrix, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax[1])
    ax[0].set_title('Heatmap of Features (Before Dropping)')
    ax[1].set_title('Absolute Correlation Matrix of Features (Before Dropping)')
    plt.savefig(fig_path)
    plt.show()

def plot_cm(cm):
    """plot confusion matrix"""
    sns.heatmap(cm, annot=True, cmap=sns.light_palette("blue"), fmt="g")
    plt.xlabel('Predicted Class')
    plt.ylabel('Original Class')
    plt.title("Confusion matrix")
    plt.show()


def plot_roc_curve(fpr_tr, tpr_tr,fpr_te, tpr_te):
    '''
    plot the ROC curve for the FPR and TPR value
    '''
    plt.plot(fpr_te, tpr_te, 'k.-', color='orange', label='ROC_test AUC:%.3f'% auc(fpr_te, tpr_te))
    plt.plot(fpr_tr, tpr_tr, 'k.-', color='green', label='ROC_train AUC:%.3f'% auc(fpr_tr, tpr_tr))
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()
    