# DB2ADMIN.USAEDIDEFINITION

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `EDISPECIFICATION`, `SEGMENT`, `SEQUENCE`, `ORDERPARTNERTYPE`, `ORDERPARTNERCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107731

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EDISPECIFICATION` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `SEGMENT` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `ORDERPARTNERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 5 | `ORDERPARTNERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `VALUE` | CHAR(15) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USAEDIDEFINITION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USAEDIDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EDISPECIFICATION,
       t.SEGMENT,
       t.SEQUENCE,
       t.ORDERPARTNERTYPE,
       t.ORDERPARTNERCODE,
       t.VALUE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USAEDIDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
