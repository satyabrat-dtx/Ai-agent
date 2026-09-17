# DB2ADMIN.QAINPROCESSMATERIALWC

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `PLANTCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85101

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `PLANTCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `PLANTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 5 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QAINPROCESSMATERIALWC.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAINPROCESSMATERIALWC.COMPANYCODE = DIVISION.COMPANYCODE AND QAINPROCESSMATERIALWC.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAINPROCESSMATERIALWC.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND QAINPROCESSMATERIALWC.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QAINPROCESSMATERIALWC.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND QAINPROCESSMATERIALWC.PLANTCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QAINPROCESSMATERIALWCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.PLANTCOMPANYCODE,
       t.PLANTCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.QAINPROCESSMATERIALWC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
