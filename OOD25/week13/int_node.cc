#include "int_node.h"

#include <string>

#include "node.h"
#include "string_node.h"

IntNode::IntNode(int value, Node* left, Node* right)
    : Node(left, right), value_(value) {}

void IntNode::Visit(Visitor* visitor) {
  visitor->EnterIntNode(this);
  // if (this->left_ != nullptr) {
  //   if (auto* left_int = dynamic_cast<IntNode*>(this->left_)) {
  //     visitor->EnterIntNode(left_int);
  //   } else if (auto* left_string = dynamic_cast<StringNode*>(this->left_)) {
  //     visitor->EnterStringNode(left_string);
  //   }
  // }
  //
  // if (this->right_ != nullptr) {
  //   if (auto* right_int = dynamic_cast<IntNode*>(this->right_)) {
  //     visitor->EnterIntNode(right_int);
  //   } else if (auto* right_string = dynamic_cast<StringNode*>(this->right_))
  //   {
  //     visitor->EnterStringNode(right_string);
  //   }
  // }
  //
  // visitor->ExitIntNode(this);
}

std::string IntNode::value() {
  return "(Int " + std::to_string(this->value_) + ")";
}
