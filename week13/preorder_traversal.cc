#include "preorder_traversal.h"

#include <string>

#include "int_node.h"
#include "string_node.h"

// 부모 먼저 들어가면서 값 추가
void PreorderTraversal::EnterIntNode(IntNode* node) {
  this->ExitIntNode(node);

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
}

void PreorderTraversal::ExitIntNode(IntNode* node) {
  if (!this->result_.empty()) {
    this->result_ += "::";
  }
  this->result_ += node->value();
}

void PreorderTraversal::EnterStringNode(StringNode* node) {
  this->ExitStringNode(node);

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
}

void PreorderTraversal::ExitStringNode(StringNode* node) {
  if (!this->result_.empty()) {
    this->result_ += "::";
  }
  this->result_ += node->value();
}

std::string PreorderTraversal::Result() { return this->result_; }
