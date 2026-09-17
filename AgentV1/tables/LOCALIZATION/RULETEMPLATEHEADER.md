# DB2ADMIN.RULETEMPLATEHEADER

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 6 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31119

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `USEDFORBOMCOMPONENT` | SMALLINT | NOT NULL |  |  |  |
| 6 | `USEDFORROUTINGSTEP` | SMALLINT | NOT NULL |  |  |  |
| 7 | `USEDPRERULE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `USEDFOR` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `USEDINPUTENTITIES` | CHAR(90) | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `INHERITVALUES` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RULETEMPLATEHEADER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RULETEMPLATEHEADER_RULETEMPLATE` | [`RULES`](../CORE_MASTER/RULES.md) | `COMPANYCODE`, `RULETEMPLATECODE` | `RULES.COMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULES.RULETEMPLATECODE = RULETEMPLATEHEADER.CODE` |
| `RULETEMPLATEHEADER_RULETEMPLATE` | [`RULEDEFINITIONHEADER`](../LOCALIZATION/RULEDEFINITIONHEADER.md) | `COMPANYCODE`, `RULETEMPLATECODE` | `RULEDEFINITIONHEADER.COMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULEDEFINITIONHEADER.RULETEMPLATECODE = RULETEMPLATEHEADER.CODE` |
| `RULETEMPLATEHEADER_RULETEMPLATE` | [`RULECHOOSEKEYS`](../LOCALIZATION/RULECHOOSEKEYS.md) | `RULECOMPANYCODE`, `RULETEMPLATECODE` | `RULECHOOSEKEYS.RULECOMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULECHOOSEKEYS.RULETEMPLATECODE = RULETEMPLATEHEADER.CODE` |
| `RULETEMPLATEHEADER_DETAIL` | [`RULETEMPLATEDETAIL`](../LOCALIZATION/RULETEMPLATEDETAIL.md) | `RULETEMPLATEHEADERCOMPANYCODE`, `RULETEMPLATEHEADERCODE` | `RULETEMPLATEDETAIL.RULETEMPLATEHEADERCOMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULETEMPLATEDETAIL.RULETEMPLATEHEADERCODE = RULETEMPLATEHEADER.CODE` |
| `RULETEMPLATEHEADER_OUTPUTTEMPLATE` | [`RULETEMPLATEDETAIL`](../LOCALIZATION/RULETEMPLATEDETAIL.md) | `RULETEMPLATEHEADERCOMPANYCODE`, `OUTPUTTEMPLATECODE` | `RULETEMPLATEDETAIL.RULETEMPLATEHEADERCOMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULETEMPLATEDETAIL.OUTPUTTEMPLATECODE = RULETEMPLATEHEADER.CODE` |
| `RULETEMPLATEHEADER_RULETEMPLATE` | [`RULESCONFIGURATION`](../LOCALIZATION/RULESCONFIGURATION.md) | `COMPANYCODE`, `RULETEMPLATECODE` | `RULESCONFIGURATION.COMPANYCODE = RULETEMPLATEHEADER.COMPANYCODE AND RULESCONFIGURATION.RULETEMPLATECODE = RULETEMPLATEHEADER.CODE` |

## Indexes

- `RULETEMPLATEHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.USEDFORBOMCOMPONENT,
       t.USEDFORROUTINGSTEP,
       t.USEDPRERULE,
       t.USEDFOR,
       t.USEDINPUTENTITIES,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.RULETEMPLATEHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
