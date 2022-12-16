import { FC, ReactNode } from "react";

export type Props = {
  children?: ReactNode;
};

const combineComponents = (components: FC<Props>[]): FC =>
  components.reduce(
    (AccumulatedComponents, CurrentComponent: FC<Props>) =>
      ({ children }: Props) =>
        (
          <AccumulatedComponents>
            <CurrentComponent>{children}</CurrentComponent>
          </AccumulatedComponents>
        ),
    ({ children }: Props) => <>{children}</>
  );

export default combineComponents;
