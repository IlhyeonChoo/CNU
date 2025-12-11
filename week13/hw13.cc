#include <iostream>
#include <string>

#include "int_node.h"
#include "node.h"
#include "postorder_traversal.h"
#include "preorder_traversal.h"
#include "string_node.h"
#include "visitor.h"

int main() {
  // Node* node5 = new StringNode("bye", nullptr, nullptr);
  // Node* node4 = new IntNode(0, nullptr, nullptr);
  // Node* node3 = new IntNode(-42, node4, node5);
  // Node* node2 = new StringNode("hi", nullptr, nullptr);
  // Node* node1 = new IntNode(3, node2, node3);
  //
  // PreorderTraversal pre = PreorderTraversal();
  // PostorderTraversal post = PostorderTraversal();
  //
  // node1->Visit(&pre);
  // node1->Visit(&post);
  //
  // std::string expect_pre =
  //     "(Int 3)::(String hi)::(Int -42)::(Int 0)::(String bye)";
  // std::cout << "[expect] " << expect_pre << std::endl;
  // std::cout << "[actual] " << pre.Result() << std::endl;
  //
  // std::string expect_post =
  //     "(String hi)::(Int 0)::(String bye)::(Int -42)::(Int 3)";
  // std::cout << "[expect] " << expect_post << std::endl;
  // std::cout << "[actual] " << post.Result() << std::endl;

  return 0;
}
