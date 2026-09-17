# DB2ADMIN.WRKSOREQFORMAT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CODE`, `ORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146036

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 4 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 5 | `SALESDISTRICT` | CHAR(50) |  |  |  |  |
| 6 | `SALESOFFICE` | CHAR(50) |  |  |  |  |
| 7 | `CUSTOMERCODE` | CHAR(25) |  |  |  |  |
| 8 | `CUSTOMERNAME` | CHAR(50) |  |  |  |  |
| 9 | `BRAND` | CHAR(50) |  |  |  |  |
| 10 | `SUBBRAND` | CHAR(50) |  |  |  |  |
| 11 | `CUSTOMERREFNO` | CHAR(50) |  |  |  |  |
| 12 | `PRODUCTCATEGORY` | CHAR(20) |  |  |  |  |
| 13 | `WARPCOUNT` | CHAR(25) |  |  |  |  |
| 14 | `FINISHCONSTRUCT` | CHAR(25) |  |  |  |  |
| 15 | `VARIETY` | CHAR(25) |  |  |  |  |
| 16 | `SALESQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `FINISH` | CHAR(100) |  |  |  |  |
| 18 | `DUEDATE` | DATE |  |  |  |  |
| 19 | `KAMNAME` | CHAR(50) |  |  |  |  |
| 20 | `DEVELOPTYPE` | CHAR(50) |  |  |  |  |
| 21 | `SODATE` | DATE |  |  |  |  |
| 22 | `LIGHTSOURCE` | CHAR(50) |  |  |  |  |
| 23 | `LIGHTSOURCES` | CHAR(50) |  |  |  |  |
| 24 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 25 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `COMPANYDESC` | VARCHAR(200) |  |  |  |  |
| 27 | `OVERALLINS` | CHAR(100) |  |  |  |  |
| 28 | `WEFTCOUNT` | CHAR(25) |  |  |  |  |
| 29 | `WEAVE` | CHAR(25) |  |  |  |  |
| 30 | `MARKETINGEXEC` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CODE,
       t.ORDERLINE,
       t.UNIQUEID,
       t.SALESDISTRICT,
       t.SALESOFFICE,
       t.CUSTOMERCODE,
       t.CUSTOMERNAME,
       t.BRAND,
       t.SUBBRAND,
       t.CUSTOMERREFNO
FROM   DB2ADMIN.WRKSOREQFORMAT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
