# DB2ADMIN.WRKPAYROLLANALYSIS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `SERIAL`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125675

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISION` | CHAR(3) |  |  |  |  |
| 3 | `PLANT` | CHAR(8) |  |  |  |  |
| 4 | `SERIAL` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ANALYSISTYPE` | CHAR(6) | NOT NULL |  |  |  |
| 6 | `BUSINESSGROUP` | CHAR(10) |  |  |  |  |
| 7 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 8 | `DEPARTMENT` | CHAR(8) |  |  |  |  |
| 9 | `SECTION` | CHAR(6) |  |  |  |  |
| 10 | `MACHINETYPE` | CHAR(6) |  |  |  |  |
| 11 | `MACHINENO` | CHAR(6) |  |  |  |  |
| 12 | `COSTCENTER` | CHAR(20) |  |  |  |  |
| 13 | `EMPLOYEECATEG` | CHAR(6) |  |  |  |  |
| 14 | `EMPLOYEESUBCATG` | CHAR(6) |  |  |  |  |
| 15 | `GRADE` | CHAR(6) |  |  |  |  |
| 16 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 17 | `WORKLOCATIONCOUNTRY` | CHAR(3) |  |  |  |  |
| 18 | `WORKLOCATIONSTATE` | CHAR(3) |  |  |  |  |
| 19 | `WORKLOCATION` | CHAR(6) |  |  |  |  |
| 20 | `EARNINGDEDUCTIONFLAG` | CHAR(1) |  |  |  |  |
| 21 | `TYPEOFEMPLOYMENT` | CHAR(6) |  |  |  |  |
| 22 | `NATUREOFEMPLOYMENT` | CHAR(6) |  |  |  |  |
| 23 | `PAYELEMENT` | CHAR(6) |  |  |  |  |
| 24 | `PAYROLLCODE` | CHAR(3) |  |  |  |  |
| 25 | `PROCESSPERIOD` | INTEGER | NOT NULL |  |  |  |
| 26 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 27 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 28 | `ATTENDANCETYPE` | CHAR(3) |  |  |  |  |
| 29 | `CURRENCY` | CHAR(4) | NOT NULL |  |  |  |
| 30 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 31 | `AMOUNT` | DECIMAL(11,4) | NOT NULL |  |  |  |
| 32 | `LASTUPDATEDATE` | DATE | NOT NULL |  |  |  |
| 33 | `LASTUPDATETIME` | CHAR(12) | NOT NULL |  |  |  |
| 34 | `DATEUPTO` | DATE | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.DIVISION,
       t.PLANT,
       t.SERIAL,
       t.ANALYSISTYPE,
       t.BUSINESSGROUP,
       t.BUSINESSUNIT,
       t.DEPARTMENT,
       t.SECTION,
       t.MACHINETYPE,
       t.MACHINENO
FROM   DB2ADMIN.WRKPAYROLLANALYSIS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
