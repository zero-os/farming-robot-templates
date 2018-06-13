@0xec607e506528fd44;

struct Schema {
    id          @0: Text; 
    networkId   @1: Text;
    subnetMask  @2: Text;
    gateway     @3: Text;
    name        @4: Text;
    ips         @5: List(Text);
}