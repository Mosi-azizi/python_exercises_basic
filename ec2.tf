provider "aws" {
  region = "ws-west-2"
}

resource "aws_instance" "sam_ec2" {
    ami = "djjjjj"
    instance_type = "t2.micro"
    tags = {
       name = "xxxx"
    }
}


provider "aws" {
    region = "xxx"
  
}
resource "aws_instance" "name" {
  ami = "sss"
  type = "t2.micro"
  tags = {
      name = "xxx"
  }
}