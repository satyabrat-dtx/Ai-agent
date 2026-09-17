# DB2ADMIN.WRKYEARANDMONTHWISE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164326

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `WORKMILLNO` | CHAR(6) |  |  |  |  |
| 3 | `EMPNAME` | CHAR(30) |  |  |  |  |
| 4 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 5 | `WORKSHIFTNO` | CHAR(3) |  |  |  |  |
| 6 | `DATES` | DATE |  |  |  |  |
| 7 | `FINANCEMONTH` | CHAR(15) |  |  |  |  |
| 8 | `FINANCEYEAR` | INTEGER | NOT NULL |  |  |  |
| 9 | `ONROLL` | DECIMAL(9,5) |  |  |  |  |
| 10 | `JOINING` | DECIMAL(9,5) |  |  |  |  |
| 11 | `LEFT` | DECIMAL(9,5) |  |  |  |  |
| 12 | `RESIGNED` | DECIMAL(9,5) |  |  |  |  |
| 13 | `CLOSINGSTRENGTH` | DECIMAL(9,5) |  |  |  |  |
| 14 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 15 | `CATEGORYDESP` | VARCHAR(200) |  |  |  |  |
| 16 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 17 | `SUBCATEGORYDESP` | VARCHAR(200) |  |  |  |  |
| 18 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 19 | `DIVISIONDESP` | VARCHAR(200) |  |  |  |  |
| 20 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 21 | `FACTORYDESP` | VARCHAR(200) |  |  |  |  |
| 22 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 23 | `DEPARTMENTDESP` | VARCHAR(200) |  |  |  |  |
| 24 | `SECTIONCODE` | CHAR(6) |  |  |  |  |
| 25 | `SECTIONDESP` | VARCHAR(200) |  |  |  |  |
| 26 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKYEARANDMONTHWISEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.WORKMILLNO,
       t.EMPNAME,
       t.GENDER,
       t.WORKSHIFTNO,
       t.DATES,
       t.FINANCEMONTH,
       t.FINANCEYEAR,
       t.ONROLL,
       t.JOINING,
       t.LEFT
FROM   DB2ADMIN.WRKYEARANDMONTHWISE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
