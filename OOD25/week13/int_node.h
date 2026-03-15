#ifndef _INT_NODE_H
#define _INT_NODE_H

#include <iostream>
#include <string>

#include "node.h"

class IntNode : public Node {
 public:
  explicit IntNode(int value, Node* left, Node* right);
  void Visit(Visitor* visitor) override;
  std::string value() override;

 private:
  int value_;
};

#endif  // _INT_NODE_H
