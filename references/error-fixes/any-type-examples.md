# Any Type Errors —— 详细代码示例

本文档为 [`any_type_errors.md`](./any_type_errors.md) 配套示例，含 Wrong/Right 对照与替代方案（interface / union / generics / type guards / type aliases）。
## Wrong / Correct 对照

### ❌ Wrong Usage
```typescript
// ❌ Wrong: Using any type
let data: any = { name: 'John', age: 30 };

// ❌ Wrong: Using any in function parameters
function processData(input: any): void {
  console.info(input.name);
}

// ❌ Wrong: Using any in event handlers
function handleEvent(event: any): void {
  console.info(event.target);
}

// ❌ Wrong: Using unknown type
let value: unknown = 'Hello';
```

### ✅ Correct Usage
```typescript
// ✅ Correct: Using explicit type
let data: { name: string; age: number } = { name: 'John', age: 30 };

// ✅ Correct: Using interface
interface UserData {
  name: string;
  age: number;
}

function processData(input: UserData): void {
  console.info(input.name);
}

// ✅ Correct: Using explicit event type
function handleEvent(event: ClickEvent): void {
  console.info(event.target.toString());
}
```

## Interface Definitions

### Simple Interface
```typescript
interface UserData {
  name: string;
  age: number;
  email?: string;
}

@Component
struct UserComponent {
  @State user: UserData = { name: 'John', age: 30 };

  private displayUser(data: UserData): string {
    return `${data.name}, ${data.age}`;
  }

  build() {
    Text(this.displayUser(this.user))
  }
}
```

### Nested Interface
```typescript
interface Address {
  street: string;
  city: string;
  zipCode: string;
}

interface User {
  id: number;
  name: string;
  address: Address;
}

@Component
struct AddressComponent {
  @State user: User = {
    id: 1,
    name: 'John',
    address: { street: '123 Main St', city: 'New York', zipCode: '10001' }
  };

  private displayAddress(user: User): string {
    return `${user.address.street}, ${user.address.city}`;
  }

  build() {
    Text(this.displayAddress(this.user))
  }
}
```

## Union Types

### Simple Union
```typescript
type StringOrNumber = string | number;

@Component
struct UnionExample {
  @State value: StringOrNumber = 'Hello';

  private displayValue(value: StringOrNumber): string {
    if (typeof value === 'string') {
      return value;
    } else {
      return value.toString();
    }
  }

  build() {
    Text(this.displayValue(this.value))
  }
}
```

### Complex Union
```typescript
type EventData = ClickEvent | TouchEvent | ScrollEvent;

@Component
struct EventExample {
  private handleEvent(event: EventData): void {
    if (event instanceof ClickEvent) {
      console.info('Click event');
    } else if (event instanceof TouchEvent) {
      console.info('Touch event');
    } else {
      console.info('Scroll event');
    }
  }

  build() {
    Column() {
      Button('Click')
        .onClick((event: ClickEvent) => this.handleEvent(event))
    }
  }
}
```

## Generics

### Simple Generic
```typescript
@Component
struct GenericExample {
  @State items: number[] = [1, 2, 3, 4, 5];

  private findItem<T>(array: T[], predicate: (item: T) => boolean): T | undefined {
    for (const item of array) {
      if (predicate(item)) {
        return item;
      }
    }
    return undefined;
  }

  build() {
    Column() {
      Button('Find Item')
        .onClick(() => {
          const found = this.findItem(this.items, (item) => item > 3);
          console.info(`Found: ${found}`);
        })
    }
  }
}
```

### Generic Class
```typescript
class Storage<T> {
  private data: T[] = [];

  add(item: T): void {
    this.data.push(item);
  }

  get(index: number): T | undefined {
    return this.data[index];
  }

  find(predicate: (item: T) => boolean): T | undefined {
    return this.data.find(predicate);
  }
}

@Component
struct StorageExample {
  private storage: Storage<number> = new Storage<number>();

  aboutToAppear() {
    this.storage.add(1);
    this.storage.add(2);
    this.storage.add(3);
  }

  build() {
    Column() {
      Button('Get Item')
        .onClick(() => {
          const item = this.storage.get(0);
          console.info(`Item: ${item}`);
        })
    }
  }
}
```

## Type Guards

### Discriminated Union
```typescript
interface StringData {
  type: 'string';
  value: string;
}

interface NumberData {
  type: 'number';
  value: number;
}

type Data = StringData | NumberData;

@Component
struct TypeGuardExample {
  @State data: Data = { type: 'string', value: 'Hello' };

  private processData(data: Data): string {
    if (data.type === 'string') {
      return data.value;
    } else {
      return data.value.toString();
    }
  }

  build() {
    Text(this.processData(this.data))
  }
}
```

## Type Aliases

### Simple Alias
```typescript
type UserId = number;
type UserName = string;
type UserEmail = string;

interface User {
  id: UserId;
  name: UserName;
  email: UserEmail;
}

@Component
struct AliasExample {
  @State user: User = { id: 1, name: 'John', email: 'john@example.com' };

  build() {
    Text(`${this.user.name} (${this.user.id})`)
  }
}
```

### Function Alias
```typescript
type EventHandler = (event: ClickEvent) => void;
type ValueHandler = (value: string) => void;

@Component
struct FunctionAliasExample {
  private onClick: EventHandler = (event: ClickEvent): void => {
    console.info('Clicked');
  };

  private onInput: ValueHandler = (value: string): void => {
    console.info(`Input: ${value}`);
  };

  build() {
    Column() {
      Button('Click')
        .onClick(this.onClick)
    }
  }
}
```
