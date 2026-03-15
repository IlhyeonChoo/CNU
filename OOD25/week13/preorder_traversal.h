#ifndef _PREORDER_TRAVERSAL_H
#define _PREORDER_TRAVERSAL_H

#include <iostream>

#include "int_node.h"
#include "string_node.h"
#include "visitor.h"

class PreorderTraversal : public Visitor {
 public:
  void EnterIntNode(IntNode* node) override;
  void ExitIntNode(IntNode* node) override;
  void EnterStringNode(StringNode* node) override;
  void ExitStringNode(StringNode* node) override;
  std::string Result() override;

 private:
  std::string result_;
};

#endif  // _PREORDER_TRAVERSAL_H
