#ifndef _STRING_NODE_h
#define _STRING_NODE_h

#include <iostream>
#include <string>

#include "node.h"

class StringNode : public Node {
 public:
  explicit StringNode(std::string value, Node* left, Node* right);
  void Visit(Visitor* visitor) override;
  std::string value() override;

 private:
  std::string value_;
};

#endif  // _STRING_NODE_h
