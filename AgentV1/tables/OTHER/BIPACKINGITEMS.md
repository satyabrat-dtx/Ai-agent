# DB2ADMIN.BIPACKINGITEMS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34183

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `USERFIELD01` | CHAR(20) |  |  |  |  |
| 2 | `USERFIELD02` | CHAR(20) |  |  |  |  |
| 3 | `USERFIELD03` | CHAR(20) |  |  |  |  |
| 4 | `USERFIELD04` | CHAR(20) |  |  |  |  |
| 5 | `USERFIELD05` | CHAR(20) |  |  |  |  |
| 6 | `USERFIELD06` | CHAR(20) |  |  |  |  |
| 7 | `USERFIELD07` | CHAR(20) |  |  |  |  |
| 8 | `USERFIELD08` | CHAR(20) |  |  |  |  |
| 9 | `USERFIELD09` | CHAR(20) |  |  |  |  |
| 10 | `USERFIELD10` | CHAR(20) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BIPACKINGITEMS.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BIPACKINGITEMSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.USERFIELD01,
       t.USERFIELD02,
       t.USERFIELD03,
       t.USERFIELD04,
       t.USERFIELD05,
       t.USERFIELD06,
       t.USERFIELD07,
       t.USERFIELD08,
       t.USERFIELD09,
       t.USERFIELD10,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BIPACKINGITEMS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
