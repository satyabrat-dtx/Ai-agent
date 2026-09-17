# DB2ADMIN.WRKFINPERIODBALANCEREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 54
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 100474

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 6 | `ACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 7 | `GLACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 8 | `SYNTHETICACCOUNTCODE` | CHAR(10) |  |  |  |  |
| 9 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `CUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 12 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 13 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 14 | `LINETYPE` | CHAR(1) |  |  |  |  |
| 15 | `FISCALYEAR` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 16 | `MARKSHORTFISCALYEAR` | CHAR(1) |  |  |  |  |
| 17 | `PERIOD` | INTEGER | NOT NULL |  |  |  |
| 18 | `INFOTYPECODE` | CHAR(2) |  |  |  |  |
| 19 | `OPENINGBALANCECREDIT` | DECIMAL(17,2) |  |  |  |  |
| 20 | `OPENINGBALANCEDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 21 | `OPENINGBALANCESIGNED` | DECIMAL(17,2) |  |  |  |  |
| 22 | `PERIODVALUEDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 23 | `PERIODVALUECREDIT` | DECIMAL(17,2) |  |  |  |  |
| 24 | `PERIODBALANCEDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 25 | `PERIODBALANCECREDIT` | DECIMAL(17,2) |  |  |  |  |
| 26 | `PERIODBALANCESIGNED` | DECIMAL(17,2) |  |  |  |  |
| 27 | `CUMULATIVEVALUEDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 28 | `CUMULATIVEVALUECREDIT` | DECIMAL(17,2) |  |  |  |  |
| 29 | `CUMULATIVEBALANCEDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 30 | `CUMULATIVEBALANCECREDIT` | DECIMAL(17,2) |  |  |  |  |
| 31 | `CUMULATIVEBALANCESIGNED` | DECIMAL(17,2) |  |  |  |  |
| 32 | `CLOSINGBALANCEDEBIT` | DECIMAL(17,2) |  |  |  |  |
| 33 | `CLOSINGBALANCECREDIT` | DECIMAL(17,2) |  |  |  |  |
| 34 | `CLOSINGBALANCESIGNED` | DECIMAL(17,2) |  |  |  |  |
| 35 | `TRANSACTIONBALANCEYEAR` | DECIMAL(17,2) |  |  |  |  |
| 36 | `CLOSINGBALANCEYEAR` | DECIMAL(17,2) |  |  |  |  |
| 37 | `SUBACCOUNTLEGALNAME1` | VARCHAR(100) |  |  |  |  |
| 38 | `SUBACCOUNTLEGALNAME2` | VARCHAR(100) |  |  |  |  |
| 39 | `SUBACCOUNTPOSTALCODE` | CHAR(20) |  |  |  |  |
| 40 | `SUBACCOUNTTOWN` | VARCHAR(100) |  |  |  |  |
| 41 | `SUBACCOUNTBUSINESSPARTNERCODE` | DECIMAL(8,0) |  |  |  |  |
| 42 | `SUBACCOUNTCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 43 | `SUBACCFINANCEACCOUNTGROUPCODE` | CHAR(10) |  |  |  |  |
| 44 | `GENERALLEDGERACCOUNTTYPE` | CHAR(1) |  |  |  |  |
| 45 | `GENERALLEDGERACCOUNTUSAGE` | CHAR(2) |  |  |  |  |
| 46 | `GENERALLDGRACCTAXTREATMENT` | CHAR(2) |  |  |  |  |
| 47 | `GENERALLEDGERACCOUNTGROUP` | CHAR(10) |  |  |  |  |
| 48 | `PRINTLEVEL` | CHAR(1) |  |  |  |  |
| 49 | `SUMLVL` | CHAR(1) |  |  |  |  |
| 50 | `INCLUDESUBLEDGER` | SMALLINT | NOT NULL |  |  |  |
| 51 | `ONLYBALANCE` | SMALLINT | NOT NULL |  |  |  |
| 52 | `ONLYTRANSACTIONS` | SMALLINT | NOT NULL |  |  |  |
| 53 | `ALLACCOUNTS` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CURRENCYCODE,
       t.ACCOUNTCODE,
       t.GLACCOUNTCODE,
       t.SYNTHETICACCOUNTCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.LONGDESCRIPTION
FROM   DB2ADMIN.WRKFINPERIODBALANCEREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
