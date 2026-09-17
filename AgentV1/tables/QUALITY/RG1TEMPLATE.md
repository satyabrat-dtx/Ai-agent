# DB2ADMIN.RG1TEMPLATE

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142496

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RG1TEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RG1TEMPLATE_SEQDEF` | [`RG1SEQDEF`](../QUALITY/RG1SEQDEF.md) | `RG1TEMPLATECOMPANYCODE`, `RG1TEMPLATEDIVISIONCODE`, `RG1TEMPLATECODE` | `RG1SEQDEF.RG1TEMPLATECOMPANYCODE = RG1TEMPLATE.COMPANYCODE AND RG1SEQDEF.RG1TEMPLATEDIVISIONCODE = RG1TEMPLATE.DIVISIONCODE AND RG1SEQDEF.RG1TEMPLATECODE = RG1TEMPLATE.CODE` |
| `RG1TEMPLATE_RG1TEMPLATE` | [`RG1TRANSACTION`](../QUALITY/RG1TRANSACTION.md) | `COMPANYCODE`, `DIVISIONCODE`, `RG1TEMPLATECODE` | `RG1TRANSACTION.COMPANYCODE = RG1TEMPLATE.COMPANYCODE AND RG1TRANSACTION.DIVISIONCODE = RG1TEMPLATE.DIVISIONCODE AND RG1TRANSACTION.RG1TEMPLATECODE = RG1TEMPLATE.CODE` |

## Indexes

- `RG1TEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.RG1TEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
