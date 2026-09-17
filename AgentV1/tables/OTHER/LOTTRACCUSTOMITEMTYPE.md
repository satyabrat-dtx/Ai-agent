# DB2ADMIN.LOTTRACCUSTOMITEMTYPE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112687

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SELECTTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 4 | `SELECTTYPE2UGGNUMBER` | CHAR(1) |  |  |  |  |
| 5 | `SELECTTYPE2UGGVALUE` | CHAR(10) |  |  |  |  |
| 6 | `SELECTTYPE3UGGNUMBER` | CHAR(1) |  |  |  |  |
| 7 | `SELECTTYPE3ADNAMENAME` | CHAR(50) |  |  |  |  |
| 8 | `SELECTTYPE3ADFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 9 | `SELECTTYPE3ADVALUE` | CHAR(20) |  |  |  |  |
| 10 | `SELECTTYPE4ADNAMENAME` | CHAR(50) |  |  |  |  |
| 11 | `SELECTTYPE4ADFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 12 | `SELECTTYPE4ADVALUE` | CHAR(20) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LOTTRACCUSTOMITEMTYPE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LOTTRACCUSTOMITEMTYPE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND LOTTRACCUSTOMITEMTYPE.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOTTRACCUSTOMITEMTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SELECTTYPE,
       t.SELECTTYPE2UGGNUMBER,
       t.SELECTTYPE2UGGVALUE,
       t.SELECTTYPE3UGGNUMBER,
       t.SELECTTYPE3ADNAMENAME,
       t.SELECTTYPE3ADFIELDNAME,
       t.SELECTTYPE3ADVALUE,
       t.SELECTTYPE4ADNAMENAME,
       t.SELECTTYPE4ADFIELDNAME
FROM   DB2ADMIN.LOTTRACCUSTOMITEMTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
