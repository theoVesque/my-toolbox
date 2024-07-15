import Link from "next/link";

const MathematicsLayout = () => {
  return (
    <div className="flex flex-col">
      <div className="flex justify-center items-center gap-x-4	 mt-8 mb-4 font-semibold text-lg bg-[#FF8181] w-fit px-6 py-3 rounded-lg">
        {" "}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width={20}
          height={20}
          viewBox="0 0 24 24"
        >
          <path
            fill="#111421"
            d="M12.125 1H22v22H2V1.83l10.125 10zm2 20H20v-1.333h-3.15v-2H20v-1.334h-3.15v-2H20V13h-3.15v-2H20V9.667h-3.15v-2H20V6.333h-3.15v-2H20V3h-5.875zm-2 0v-6.36L4 6.615V21z"
          ></path>
        </svg>
        <h2 className="">Mathematics tools</h2>
      </div>

      <div className="flex flex-wrap gap-x-2 lg:gap-x-4 gap-y-4">
        <div>
          {" "}
          <Link
            href="/tools/converter"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Converter
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/percent"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Percent
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/sum"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Sum
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/average"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Average
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/median"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Median
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/standardDeviation"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Standard deviation
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/maximum_in_list"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Maximum in list
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/minimum_in_list"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Minimum in list
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/power"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Power
          </Link>
        </div>

        <div>
          {" "}
          <Link
            href="/tools/mathematics/factorial"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Factorial
          </Link>
        </div>
        <div>
          {" "}
          <Link
            href="/tools/mathematics/factorial"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Factorial
          </Link>
        </div>
        <div>
          {" "}
          <Link
            href="/tools/mathematics/factorial"
            className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
          >
            Factorial
          </Link>
        </div>
      </div>
    </div>
  );
};

export default MathematicsLayout;
