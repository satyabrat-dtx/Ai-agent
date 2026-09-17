# DB2ADMIN.WRKFINREGISTER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CREATIONTIME`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178573

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIME` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `CODE` | CHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `NAMEOFPARTY` | VARCHAR(200) |  |  |  |  |
| 6 | `INVOICEDATE` | DATE |  |  |  |  |
| 7 | `POSTINGDATE` | DATE |  |  |  |  |
| 8 | `TIN` | CHAR(20) |  |  |  |  |
| 9 | `PAN` | CHAR(10) |  |  |  |  |
| 10 | `CST` | CHAR(20) |  |  |  |  |
| 11 | `MRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 12 | `ITEMTYPE` | CHAR(3) |  |  |  |  |
| 13 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `STATE` | VARCHAR(80) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINREGISTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIME,
       t.LINENO,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.NAMEOFPARTY,
       t.INVOICEDATE,
       t.POSTINGDATE,
       t.TIN,
       t.PAN,
       t.CST,
       t.MRNPREFIXCODE
FROM   DB2ADMIN.WRKFINREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
