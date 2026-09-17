# DB2ADMIN.WRKEMPATTENDANCEDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `EMPCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170554

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `WORKMILLNO` | CHAR(6) |  |  |  |  |
| 3 | `EMPCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `EMPNAME` | VARCHAR(200) |  |  |  |  |
| 5 | `GENDER` | INTEGER | NOT NULL |  |  |  |
| 6 | `WORKSHIFTNO` | CHAR(3) |  |  |  |  |
| 7 | `ONROLL` | INTEGER | NOT NULL |  |  |  |
| 8 | `ONLEAVENOS` | DECIMAL(9,5) |  |  |  |  |
| 9 | `ONWEEKLYOFFNOS` | DECIMAL(9,5) |  |  |  |  |
| 10 | `ONABSENTNOS` | DECIMAL(9,5) |  |  |  |  |
| 11 | `ACTUALAVAILABLENOS` | DECIMAL(9,5) |  |  |  |  |
| 12 | `CATEGORYCODE` | CHAR(10) |  |  |  |  |
| 13 | `CATEGORYDESP` | VARCHAR(200) |  |  |  |  |
| 14 | `SUBCATEGORYCODE` | CHAR(10) |  |  |  |  |
| 15 | `SUBCATEGORYDESP` | VARCHAR(200) |  |  |  |  |
| 16 | `DIVISIONCODE` | CHAR(10) |  |  |  | Division within a company; second-level organisational discriminator. |
| 17 | `DIVISIONDESP` | VARCHAR(200) |  |  |  |  |
| 18 | `FACTORYCODE` | CHAR(10) |  |  |  |  |
| 19 | `FACTORYDESP` | VARCHAR(200) |  |  |  |  |
| 20 | `DEPARTMENTCODE` | CHAR(10) |  |  |  |  |
| 21 | `DEPARTMENTDESP` | VARCHAR(200) |  |  |  |  |
| 22 | `SECTIONCODE` | CHAR(6) |  |  |  |  |
| 23 | `SECTIONDESP` | VARCHAR(200) |  |  |  |  |
| 24 | `BIRTHDATE` | DATE |  |  |  |  |
| 25 | `JOININGDATE` | DATE |  |  |  |  |
| 26 | `EXITDATE` | DATE |  |  |  |  |
| 27 | `DATEDIFFERENCE` | INTEGER | NOT NULL |  |  |  |
| 28 | `EXITDATEDIFF` | INTEGER | NOT NULL |  |  |  |
| 29 | `DISCONDATEDIFF` | INTEGER | NOT NULL |  |  |  |
| 30 | `JOININGDATEDIFF` | INTEGER | NOT NULL |  |  |  |
| 31 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKEMPATTENDANCEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.WORKMILLNO,
       t.EMPCODE,
       t.EMPNAME,
       t.GENDER,
       t.WORKSHIFTNO,
       t.ONROLL,
       t.ONLEAVENOS,
       t.ONWEEKLYOFFNOS,
       t.ONABSENTNOS,
       t.ACTUALAVAILABLENOS
FROM   DB2ADMIN.WRKEMPATTENDANCEDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
