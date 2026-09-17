# DB2ADMIN.APPORDERPARTNERUOMS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110830

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `BASEUOMCODECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `ORDERUOMCODECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `UNITOFMEASURE_BASEUOMCODE` | `BASEUOMCODECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `APPORDERPARTNERUOMS.BASEUOMCODECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_ORDERUOMCODE` | `ORDERUOMCODECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `APPORDERPARTNERUOMS.ORDERUOMCODECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPORDERPARTNERUOMSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.BASEUOMCODECODE,
       t.ORDERUOMCODECODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPORDERPARTNERUOMS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
