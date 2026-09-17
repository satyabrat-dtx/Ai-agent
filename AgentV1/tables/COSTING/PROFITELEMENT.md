# DB2ADMIN.PROFITELEMENT

- **Module**: `COSTING` (low confidence — FK neighbourhood: 2 of 2 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 196450

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `INPUTFROM` | CHAR(1) |  |  |  |  |
| 6 | `PROFIT` | SMALLINT | NOT NULL |  |  |  |
| 7 | `COSTLEVELCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `COSTLEVELCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PROFITELEMENT.COMPANYCODE = COMPANY.CODE` |
| `COSTLEVEL_COSTLEVEL` | `COSTLEVELCOMPANYCODE`, `COSTLEVELCODE` | [`COSTLEVEL`](../COSTING/COSTLEVEL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROFITELEMENT.COSTLEVELCOMPANYCODE = COSTLEVEL.COMPANYCODE AND PROFITELEMENT.COSTLEVELCODE = COSTLEVEL.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PROFITELEMENT_PROFITELEMENT` | [`COSTSIMPROFITELEMENTS`](../COSTING/COSTSIMPROFITELEMENTS.md) | `COMPANYCODE`, `PROFITELEMENTCODE` | `COSTSIMPROFITELEMENTS.COMPANYCODE = PROFITELEMENT.COMPANYCODE AND COSTSIMPROFITELEMENTS.PROFITELEMENTCODE = PROFITELEMENT.CODE` |
| `PROFITELEMENT_FORMULA` | [`PROFITELEMENTFORMULA`](../COSTING/PROFITELEMENTFORMULA.md) | `PROFITELEMENTCOMPANYCODE`, `PROFITELEMENTCODE` | `PROFITELEMENTFORMULA.PROFITELEMENTCOMPANYCODE = PROFITELEMENT.COMPANYCODE AND PROFITELEMENTFORMULA.PROFITELEMENTCODE = PROFITELEMENT.CODE` |
| `PROFITELEMENT_REFPROFITELEMENT` | [`PROFITELEMENTFORMULA`](../COSTING/PROFITELEMENTFORMULA.md) | `PROFITELEMENTCOMPANYCODE`, `REFPROFITELEMENTCODE` | `PROFITELEMENTFORMULA.PROFITELEMENTCOMPANYCODE = PROFITELEMENT.COMPANYCODE AND PROFITELEMENTFORMULA.REFPROFITELEMENTCODE = PROFITELEMENT.CODE` |

## Indexes

- `PROFITELEMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.INPUTFROM,
       t.PROFIT,
       t.COSTLEVELCOMPANYCODE,
       t.COSTLEVELCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PROFITELEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
