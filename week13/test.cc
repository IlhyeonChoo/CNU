#include <gtest/gtest.h>

#include "int_node.h"
#include "postorder_traversal.h"
#include "preorder_traversal.h"
#include "string_node.h"

class VisitTest : public ::testing::Test {
 public:
  IntNode* int_3;
  IntNode* int_2;
  IntNode* int_1;
  StringNode* string_3;
  StringNode* string_2;
  StringNode* string_1;

 protected:
  void SetUp() override {
    int_3 = new IntNode(3, nullptr, nullptr);
    int_2 = new IntNode(2, nullptr, nullptr);
    int_1 = new IntNode(1, int_2, int_3);

    string_3 = new StringNode("c", nullptr, nullptr);
    string_2 = new StringNode("b", nullptr, nullptr);
    string_1 = new StringNode("a", string_2, string_3);
  }

  void TearDown() override {
    delete int_1;
    delete int_2;
    delete int_3;
    delete string_1;
    delete string_2;
    delete string_3;
  }
};

TEST_F(VisitTest, PreIntTest) {
  PreorderTraversal pre;
  int_1->Visit(&pre);
  EXPECT_EQ(pre.Result(), "(Int 1)::(Int 2)::(Int 3)");
}

TEST_F(VisitTest, PostIntTest) {
  PostorderTraversal post;
  int_1->Visit(&post);
  EXPECT_EQ(post.Result(), "(Int 2)::(Int 3)::(Int 1)");
}

TEST_F(VisitTest, PreStringTest) {
  PreorderTraversal pre;
  string_1->Visit(&pre);
  EXPECT_EQ(pre.Result(), "(String a)::(String b)::(String c)");
}

TEST_F(VisitTest, PostStringTest) {
  PostorderTraversal post;
  string_1->Visit(&post);
  EXPECT_EQ(post.Result(), "(String b)::(String c)::(String a)");
}

TEST_F(VisitTest, PreMixTest1) {
  StringNode* s_left = new StringNode("left", nullptr, nullptr);
  StringNode* s_right = new StringNode("right", nullptr, nullptr);
  IntNode* root = new IntNode(100, s_left, s_right);

  PreorderTraversal pre;
  root->Visit(&pre);
  EXPECT_EQ(pre.Result(), "(Int 100)::(String left)::(String right)");

  delete root;
  delete s_left;
  delete s_right;
}

TEST_F(VisitTest, PostMixTest1) {
  StringNode* s_left = new StringNode("left", nullptr, nullptr);
  StringNode* s_right = new StringNode("right", nullptr, nullptr);
  IntNode* root = new IntNode(100, s_left, s_right);

  PostorderTraversal post;
  root->Visit(&post);
  EXPECT_EQ(post.Result(), "(String left)::(String right)::(Int 100)");

  delete root;
  delete s_left;
  delete s_right;
}

TEST_F(VisitTest, PreMixTest2) {
  IntNode* i_left = new IntNode(10, nullptr, nullptr);
  IntNode* i_right = new IntNode(20, nullptr, nullptr);
  StringNode* root = new StringNode("root", i_left, i_right);

  PreorderTraversal pre;
  root->Visit(&pre);
  EXPECT_EQ(pre.Result(), "(String root)::(Int 10)::(Int 20)");

  delete root;
  delete i_left;
  delete i_right;
}

TEST_F(VisitTest, PostMixTest2) {
  IntNode* i_left = new IntNode(10, nullptr, nullptr);
  IntNode* i_right = new IntNode(20, nullptr, nullptr);
  StringNode* root = new StringNode("root", i_left, i_right);

  PostorderTraversal post;
  root->Visit(&post);
  EXPECT_EQ(post.Result(), "(Int 10)::(Int 20)::(String root)");

  delete root;
  delete i_left;
  delete i_right;
}

TEST_F(VisitTest, PreIncompleteTest) {
  IntNode* root = new IntNode(999, int_1, nullptr);

  PreorderTraversal pre;
  root->Visit(&pre);
  EXPECT_EQ(pre.Result(), "(Int 999)::(Int 1)::(Int 2)::(Int 3)");

  delete root;
}

TEST_F(VisitTest, PostIncompleteTest) {
  IntNode* root = new IntNode(999, int_1, nullptr);

  PostorderTraversal post;
  root->Visit(&post);
  EXPECT_EQ(post.Result(), "(Int 2)::(Int 3)::(Int 1)::(Int 999)");

  delete root;
}
