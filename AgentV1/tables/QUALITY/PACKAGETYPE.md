# DB2ADMIN.PACKAGETYPE

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `PACKAGETYPE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 122954

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PACKAGETYPE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `TAREWEIGHT` | DECIMAL(6,2) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PACKAGETYPE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PACKAGETYPE_PACKAGETYPE` | [`ELEMENTSCUTTING`](../QUALITY/ELEMENTSCUTTING.md) | `COMPANYCODE`, `PACKAGETYPEPACKAGETYPE` | `ELEMENTSCUTTING.COMPANYCODE = PACKAGETYPE.COMPANYCODE AND ELEMENTSCUTTING.PACKAGETYPEPACKAGETYPE = PACKAGETYPE.PACKAGETYPE` |

## Indexes

- `PACKAGETYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PACKAGETYPE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TAREWEIGHT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PACKAGETYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
