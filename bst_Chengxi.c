
已開啟會話群組。1 封未讀郵件。

移至內容
透過螢幕閱讀器使用 Gmail
1
搜尋



Gmail
撰寫
標籤
收件匣
已加星號
重要郵件
寄件備份
草稿 (1)
類別
社交網路 (421)
促銷內容 (2,559)
最新快訊 (1)
論壇
私人
旅遊
Notes
OSU
更多 
Hangouts

 
 
 
  更多 
第 1 個，共 1,480 個  
 
全部列印 開啟新視窗
Fwd: 作业 
收件匣
x 

Yang, Chengxi <yangchen@oregonstate.edu>
附件22:46 (0 分鐘前)

寄給 我 
英文
中文（繁體）   翻譯郵件
關閉下列語言的翻譯功能：英文
---------- Forwarded message ----------
From: Yang, Chengxi <yangchen@oregonstate.edu>
Date: Thu, Nov 9, 2017 at 10:43 PM
Subject: 作业
To: kyujyokei@gmai.com
2 個附件 
 
	
按這裡即可回覆或轉寄郵件
您使用了 115 GB 配額中的 4.97 GB (4%)
管理
條款 - 隱私權
上次帳戶活動時間：0 分鐘前
詳細資料


/*
 * This file contains an implementation of the basic BST functions prototyped
 * in bst.h.  At the bottom of this file is where you will implement your
 * functions for this assignment.  Make sure to add your name and
 * @oregonstate.edu email address below:
 *
 * Name:
 * Email:
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "bst.h"

/*
 * This structure represents a single node in a BST.
 */
struct bst_node {
  int val;
  struct bst_node* left;
  struct bst_node* right;
};


/*
 * This structure represents an entire BST.  Note that we only need a
 * reference to the root node of the tree.
 */
struct bst {
  struct bst_node* root;
};


struct bst* bst_create() {
  struct bst* bst = malloc(sizeof(struct bst));
  assert(bst);
  bst->root = NULL;
  return bst;
}


void bst_free(struct bst* bst) {
  assert(bst);

  /*
   * Assume that bst_remove() frees each node it removes and use it to free
   * all of the nodes in the tree.
   */
  while (!bst_isempty(bst)) {
    bst_remove(bst->root->val, bst);
  }

  free(bst);
}


int bst_isempty(struct bst* bst) {
  assert(bst);
  return bst->root == NULL;
}


/*
 * Helper function to generate a single BST node containing a given value.
 */
struct bst_node* _bst_node_create(int val) {
  struct bst_node* n = malloc(sizeof(struct bst_node));
  assert(n);
  n->val = val;
  n->left = n->right = NULL;
  return n;
}


/*
 * Helper function to insert a given value into a subtree of a BST rooted at
 * a given node.  Operates recursively by determining into which subtree (left
 * or right) under the given node the value should be inserted and performing
 * the insertion on that subtree.
 *
 * Returns the root of the given subtree, modified to contain a new node with
 * the specified value.
 */
struct bst_node* _bst_subtree_insert(int val, struct bst_node* n) {

  if (n == NULL) {

    /*
     * If n is NULL, we know we've reached a place to insert val, so we
     * create a new node holding val and return it.
     */
    return _bst_node_create(val);

  } else if (val < n->val) {

    /*
     * If val is less than the value at n, we insert val in n's left subtree
     * (somewhere) and update n->left to point to the modified subtree (with
     * val inserted).
     */
    n->left = _bst_subtree_insert(val, n->left);

  } else {

    /*
     * If val is greater than or equal to the value at n, we insert val in n's
     * right subtree (somewhere) and update n->right to point to the modified
     * subtree (with val inserted).
     */
    n->right = _bst_subtree_insert(val, n->right);

  }

  /*
   * For the else if and else conditions, the subtree rooted at n has already
   * been modified (by setting n->left or n->right above), so we can just
   * return n here.
   */
  return n;

}


void bst_insert(int val, struct bst* bst) {

  assert(bst);

  /*
   * We insert val by using our subtree insertion function starting with the
   * subtree rooted at bst->root (i.e. the whole tree).
   */
  bst->root = _bst_subtree_insert(val, bst->root);

}


/*
 * Helper function to return the minimum value in a subtree of a BST.
 */
int _bst_subtree_min_val(struct bst_node* n) {
  /*
   * The minimum value in any subtree is just the leftmost value.  Keep going
   * left till we get there.
   */
  while (n->left != NULL) {
    n = n->left;
  }
  return n->val;
}


/*
 * Helper function to remove a given value from a subtree of a BST rooted at
 * a specified node.  Operates recursively by figuring out whether val is in
 * the left or the right subtree of the specified node and performing the
 * remove operation on that subtree.
 *
 * Returns the potentially new root of the given subtree, modified to have
 * the specified value removed.
 */
struct bst_node* _bst_subtree_remove(int val, struct bst_node* n) {

  if (n == NULL) {

    /*
     * If n is NULL, that means we've reached a leaf node without finding
     * the value we wanted to remove.  The tree won't be modified.
     */
    return NULL;

  } else if (val < n->val) {

    /*
     * If val is less than n, remove val from n's left subtree and update
     * n->left to point to the modified subtree (with val removed).  Return n,
     * whose subtree itself has now been modified.
     */
    n->left = _bst_subtree_remove(val, n->left);
    return n;

  } else if (val > n->val) {

    /*
     * If val is greater than n, remove val from n's right subtree and update
     * n->right to point to the modified subtree (with val removed).  Return n,
     * whose subtree itself has now been modified.
     */
    n->right = _bst_subtree_remove(val, n->right);
    return n;

  } else {

    /*
     * If we've reached this point, we've found a node with value val.  We
     * need to remove this node from the tree, and the way we do that will
     * differ based on whether the node has 0, 1, or 2 children.
     */
    if (n->left != NULL && n->right != NULL) {

      /*
       * If n has 2 children, we replace the value at n with the value at n's
       * in-order successor node, which is the minimum value in n's right
       * subtree.  Then we recursively remove n's in-order successor node from
       * the tree (specifically from n's right subtree).
       */
      n->val = _bst_subtree_min_val(n->right);
      n->right = _bst_subtree_remove(n->val, n->right);
      return n;

    } else if (n->left != NULL) {

      /*
       * If n has only a left child, we simply delete n by freeing it and
       * returning the left child node so that it becomes the new child of
       * n's parent via the recursion.
       */
      struct bst_node* left_child = n->left;
      free(n);
      return left_child;

    } else if (n->right != NULL) {

      /*
       * If n has only a right child, we simply delete n by freeing it and
       * returning the right child node so that it becomes the new child of
       * n's parent via the recursion.
       */
      struct bst_node* right_child = n->right;
      free(n);
      return right_child;

    } else {

      /*
       * Otherwise, n has no children, and we can simply free it and return
       * NULL so that n's parent will lose n as a child via the recursion.
       */
      free(n);
      return NULL;

    }

  }

}


void bst_remove(int val, struct bst* bst) {

  assert(bst);

  /*
   * We remove val by using our subtree removal function starting with the
   * subtree rooted at bst->root (i.e. the whole tree).
   */
  bst->root = _bst_subtree_remove(val, bst->root);

}


int bst_contains(int val, struct bst* bst) {

  assert(bst);

  // Iteratively search for val in bst.
  struct bst_node* cur = bst->root;
  while (cur != NULL) {

    if (val == cur->val) {

      // We found the value we're looking for in cur.
      return 1;

    } else if (val < cur->val) {

      /*
       * The value we're looking for is less than the value at cur, so we
       * branch left.
       */
      cur = cur->left;

    } else {

      /*
       * The value we're looking for is greater than or equal to the value at
       * cur, so we branch right.
       */
       cur = cur->right;

    }

  }

  /*
   * If we make it to a leaf node (i.e. cur is NULL), we didn't find what we
   * were looking for.
   */
  return 0;
}


/*****************************************************************************
 *
 * Below are the functions and structures you'll implement in this assignment.
 *
 *****************************************************************************/


/*
 * This is the structure you will use to create an in-order BST iterator.  It
 * is up to you how to define this structure.
 */
struct bst_iterator{
	struct bts_node* root;
	int tree_size;
	int* arrBuffer;
	int* curr;
};

int subtree_size(struct bst_node* subtree_root)
{
	if(subtree_root == NULL)
	{
		return 0;
	}
	else
	{
		return 1 + subtree_size(subtree_root->left) + subtree_size(subtree_root->right);
	}
}

/*
 * This function should return the total number of elements stored in a given
 * BST.
 *
 * Params:
 *   bst - the BST whose elements are to be counted
 *
 * Return:
 *   Should return the total number of elements stored in bst.
 */
int bst_size(struct bst* bst) {
  return subtree_size(bst->root);
}

int subtree_height(struct bst_node* subtree_root)
{
	if(subtree_root == NULL)
	{
		return 0;
	}
	else
	{
		int left_tree_height = subtree_height(subtree_root->left);
		int right_tree_height = subtree_height(subtree_root->right);
		return left_tree_height > right_tree_height ? left_tree_height : right_tree_height + 1;
	}
}

/*
 * This function should return the height of a given BST, which is the maximum
 * depth of any node in the tree (i.e. the number of edges in the path from
 * the root to that node).
 *
 * Params:
 *   bst - the BST whose height is to be computed
 *
 * Return:
 *   Should return the height of bst.
 */
int bst_height(struct bst* bst) {
	return subtree_height(bst->root);
}

int bst_subtree_path_sum(int sum, struct bst_node* subtree_root)
{
	if(subtree_root->left == NULL && subtree_root->right == NULL)
	{
		if(sum == subtree_root->val)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	else
	{
		int remainder = sum - subtree_root->val;
		if(subtree_root->left != NULL && subtree_root->right != NULL)
		{
			if(bst_subtree_path_sum(remainder, subtree_root->left) == 1 || bst_subtree_path_sum(remainder, subtree_root->right) == 1)
			{
				return 1;
			}
			else
			{
				return 0;
			}
		}
		else if(subtree_root->left == NULL && subtree_root->right != NULL)
		{
			if(bst_subtree_path_sum(remainder, subtree_root->right) == 1)
			{
				return 1;
			}
			else
			{
				return 0;
			}			
		}
		else if(subtree_root->left != NULL && subtree_root->right == NULL)
		{
			if(bst_subtree_path_sum(remainder, subtree_root->left) == 1)
			{
				return 1;
			}
			else
			{
				return 0;
			}				
		}
	}
}

/*
 * This function should determine whether a given BST contains a path from the
 * root to a leaf in which the node values sum to a specified value.
 *
 * Params:
 *   sum - the value to search for among the path sums of bst
 *   bst - the BST whose paths sums to search
 *
 * Return:
 *   Should return 1 if bst contains a path from the root to a leaf in which
 *   the values of the nodes add up to sum.  Should return 0 otherwise.
 */
int bst_path_sum(int sum, struct bst* bst) {
	//return 1;
  return bst_subtree_path_sum(sum, bst->root);
}

void inorder_traversal(struct bst_node* node, int* record_arr, int* index)
{
	if(node != NULL)
	{
		inorder_traversal(node->left, record_arr, index);
		record_arr[*index] = node->val;
		(*index)++;
		inorder_traversal(node->right, record_arr, index);
	}
	else
	{
		return;
	}

}

/*
 * This function should allocate and initialize a new in-order BST iterator
 * given a specific BST over which to iterate.
 *
 * Params:
 *   bst - the BST over which to perform in-order iteration.  May not be NULL.
 *
 * Return:
 *   Should return a pointer to a new in-order BST iterator, initialized so
 *   that the first value returned by bst_iterator_next() is the first in-order
 *   value in bst (i.e. the leftmost value in the tree).
 */
struct bst_iterator* bst_iterator_create(struct bst* bst) {
	struct bst_iterator* iter = malloc(sizeof(struct bst_iterator));
	iter->tree_size = bst_size(bst);
	iter->arrBuffer = malloc(sizeof(int) * iter->tree_size);
	int index = 0;
	inorder_traversal(bst->root, iter->arrBuffer, &index);
/* 	for(int i = 0;i < tree_size;i++)
	{
		printf("%d ", iter->arrBuffer[i]);
	}
	printf("\n"); */
	iter->curr = iter->arrBuffer;
  return iter;
}

/*
 * This function should free all memory allocated to a BST iterator.
 *
 * Params:
 *   iter - the iterator whose memory is to be freed.  May not be NULL.
 */
void bst_iterator_free(struct bst_iterator* iter) {
	free(iter->arrBuffer);
	free(iter);
}


/*
 * This function should return 1 if there is at least one more node to visit
 * in the in-order iteration of the BST represented by a given iterator.  If
 * there are no more nodes to visit, it should return 0.
 *
 * Params:
 *   iter - the iterator to be checked for more values.  May not be NULL.
 */
int bst_iterator_has_next(struct bst_iterator* iter) {
	if(iter->curr - iter->arrBuffer < iter->tree_size)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}


/*
 * This function should return the next value in the in-order iteration of the
 * BST represented by a given iterator.
 *
 * Params:
 *   iter - the iterator whose next value is to be returned.  May not be NULL
 *     and must have at least one more value to be returned.
 */
int bst_iterator_next(struct bst_iterator* iter) {
	int value = *(iter->curr);
	(iter->curr)++;
  return value;
}
