# DB2ADMIN.WRKFINDEPRECIATIONCLCITACT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `LINENUMBER`, `COMPANYCODE`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 180942

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENUMBER` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `BUSINESSUNITGROUP` | CHAR(10) |  |  |  |  |
| 4 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 5 | `MAINASSET` | CHAR(15) |  |  |  |  |
| 6 | `ASSETNUMBER` | CHAR(15) |  |  |  |  |
| 7 | `ASSETDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 8 | `ACQUISVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ACCMDEPRECIATION` | DECIMAL(18,5) |  |  |  |  |
| 10 | `BOOKVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `DEPFORTHECURRENTPERIOD` | DECIMAL(18,5) |  |  |  |  |
| 12 | `COSTCENTER` | CHAR(20) |  |  |  |  |
| 13 | `PROFITCENTER` | CHAR(10) |  |  |  |  |
| 14 | `CURRENCY` | CHAR(4) |  |  |  |  |
| 15 | `ADDITIONALDEP` | CHAR(2) |  |  |  |  |
| 16 | `ASSETDEBITGLCODE` | CHAR(20) |  |  |  |  |
| 17 | `ASSETCREDITGLCODE` | CHAR(20) |  |  |  |  |
| 18 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINDEPRECIATIONCLCITACTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LINENUMBER,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.BUSINESSUNITGROUP,
       t.BUSINESSUNIT,
       t.MAINASSET,
       t.ASSETNUMBER,
       t.ASSETDESCRIPTION,
       t.ACQUISVALUE,
       t.ACCMDEPRECIATION,
       t.BOOKVALUE,
       t.DEPFORTHECURRENTPERIOD
FROM   DB2ADMIN.WRKFINDEPRECIATIONCLCITACT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
