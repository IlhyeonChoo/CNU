#ifndef _POSTORDER_TRAVERSAL_H
#define _POSTORDER_TRAVERSAL_H

#include <iostream>

#include "int_node.h"
#include "string_node.h"
#include "visitor.h"

class PostorderTraversal : public Visitor {
 public:
  void EnterIntNode(IntNode* node) override;
  void ExitIntNode(IntNode* node) override;
  void EnterStringNode(StringNode* node) override;
  void ExitStringNode(StringNode* node) override;
  std::string Result() override;

 private:
  std::string result_;
};

#endif  // _POSTORDER_TRAVERSAL_H
