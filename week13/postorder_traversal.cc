#include "postorder_traversal.h"

#include <string>

// 부모를 제일 마지막 exit하면서 추가
void PostorderTraversal::EnterIntNode(IntNode* node) {
  if (node->left() != nullptr) {
    if (auto* left_node = dynamic_cast<IntNode*>(node->left())) {
      left_node->Visit(this);
    } else if (auto* left_node = dynamic_cast<StringNode*>(node->left())) {
      left_node->Visit(this);
    }
  }
  if (node->right() != nullptr) {
    if (auto* right_node = dynamic_cast<IntNode*>(node->right())) {
      right_node->Visit(this);
    } else if (auto* right_node = dynamic_cast<StringNode*>(node->right())) {
      right_node->Visit(this);
    }
  }

  this->ExitIntNode(node);
}
void PostorderTraversal::ExitIntNode(IntNode* node) {
  if (!this->result_.empty()) {
    this->result_ += "::";
  }
  this->result_ += node->value();
}

void PostorderTraversal::EnterStringNode(StringNode* node) {
  if (node->left() != nullptr) {
    if (auto* left_node = dynamic_cast<IntNode*>(node->left())) {
      left_node->Visit(this);
    } else if (auto* left_node = dynamic_cast<StringNode*>(node->left())) {
      left_node->Visit(this);
    }
  }

  if (node->right() != nullptr) {
    if (auto* right_node = dynamic_cast<IntNode*>(node->right())) {
      right_node->Visit(this);
    } else if (auto* right_node = dynamic_cast<StringNode*>(node->right())) {
      right_node->Visit(this);
    }
  }

  this->ExitStringNode(node);
}

void PostorderTraversal::ExitStringNode(StringNode* node) {
  if (!this->result_.empty()) {
    this->result_ += "::";
  }
  this->result_ += node->value();
}

std::string PostorderTraversal::Result() { return this->result_; }
