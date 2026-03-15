#include "string_node.h"

#include <string>

#include "int_node.h"
#include "visitor.h"

StringNode::StringNode(std::string value, Node* left, Node* right)
    : Node(left, right), value_(value) {}

void StringNode::Visit(Visitor* visitor) {
  visitor->EnterStringNode(this);
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
  // visitor->ExitStringNode(this);
}

std::string StringNode::value() { return "(String " + this->value_ + ")"; }
