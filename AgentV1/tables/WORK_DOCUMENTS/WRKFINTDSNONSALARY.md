# DB2ADMIN.WRKFINTDSNONSALARY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONTIMESTAMP`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 203757

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `BUSINESSUNITDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 5 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 6 | `TDSCODE` | CHAR(10) |  |  |  |  |
| 7 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `SUPPLIERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `DIVISIONCODEDEDUCTEECODE` | VARCHAR(200) |  |  |  |  |
| 10 | `REPORTMONTH` | INTEGER | NOT NULL |  |  |  |
| 11 | `FINDOCNO` | CHAR(15) |  |  |  |  |
| 12 | `DEDUCTEEFIRSTNAME` | VARCHAR(200) |  |  |  |  |
| 13 | `POSTINGDATE` | DATE |  |  |  |  |
| 14 | `DEDUCTEEMIDDLENAME` | VARCHAR(200) |  |  |  |  |
| 15 | `DEDUCTEELASTNAME` | VARCHAR(80) |  |  |  |  |
| 16 | `ADDRESS1` | VARCHAR(200) |  |  |  |  |
| 17 | `ADDRESS2` | VARCHAR(200) |  |  |  |  |
| 18 | `STATEDESC` | VARCHAR(200) |  |  |  |  |
| 19 | `PINCODE` | CHAR(20) |  |  |  |  |
| 20 | `AMOUNTOFPAYMENT` | DECIMAL(18,5) |  |  |  |  |
| 21 | `AMOUNTPAIDDATE` | DATE |  |  |  |  |
| 22 | `TAXDEDUCTIONRATE` | DECIMAL(5,2) |  |  |  |  |
| 23 | `TDSAMT` | DECIMAL(18,5) |  |  |  |  |
| 24 | `TAXDEDUCTEDDATE` | DATE |  |  |  |  |
| 25 | `PANNUMBER` | CHAR(30) |  |  |  |  |
| 26 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 27 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 28 | `DEDUCTEECODE` | CHAR(8) |  |  |  |  |
| 29 | `SUPPLIERINVOICENO` | CHAR(25) |  |  |  |  |
| 30 | `SUPPLIERINVOICEDATE` | DATE |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINTDSNONSALARYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENUMBER,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.BUSINESSUNITDESCRIPTION,
       t.FINANCIALYEARCODE,
       t.TDSCODE,
       t.SUPPLIERCODE,
       t.SUPPLIERTYPE,
       t.DIVISIONCODEDEDUCTEECODE,
       t.REPORTMONTH,
       t.FINDOCNO
FROM   DB2ADMIN.WRKFINTDSNONSALARY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
