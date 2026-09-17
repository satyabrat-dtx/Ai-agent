# DB2ADMIN.DIRECTIVETEMPLATE

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 2 of 2 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 199025

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `RUNBEFORESTANDARDRULES` | SMALLINT | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `EVALUATEALLCONDITIONS` | SMALLINT | NOT NULL |  |  |  |
| 15 | `FORCESKIPTOTRUE` | SMALLINT | NOT NULL |  |  |  |
| 16 | `KEEPSUBCODEFATHERVALUE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DIRECTIVETEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DIRECTIVETEMPLATE_DIRECTIVETEMPLATE` | [`BOMCMPDEFAULTSDIRECTIVETMP`](../ITEM_MASTER/BOMCMPDEFAULTSDIRECTIVETMP.md) | `BCDCOMPANYCODE`, `DIRECTIVETEMPLATECODE` | `BOMCMPDEFAULTSDIRECTIVETMP.BCDCOMPANYCODE = DIRECTIVETEMPLATE.COMPANYCODE AND BOMCMPDEFAULTSDIRECTIVETMP.DIRECTIVETEMPLATECODE = DIRECTIVETEMPLATE.CODE` |
| `DIRECTIVETEMPLATE_DIRECTIVETEMPLATE` | [`BOMCMPDIRTMP`](../ITEM_MASTER/BOMCMPDIRTMP.md) | `BOMCMP`, `DIRECTIVETEMPLATECODE` | `BOMCMPDIRTMP.BOMCMP = DIRECTIVETEMPLATE.COMPANYCODE AND BOMCMPDIRTMP.DIRECTIVETEMPLATECODE = DIRECTIVETEMPLATE.CODE` |
| `DIRECTIVETEMPLATE_INPUTFIELD` | [`DIRECTIVETEMPLATEINPUTFIELD`](../ITEM_MASTER/DIRECTIVETEMPLATEINPUTFIELD.md) | `DIRECTIVETEMPLATECOMPANYCODE`, `DIRECTIVETEMPLATECODE` | `DIRECTIVETEMPLATEINPUTFIELD.DIRECTIVETEMPLATECOMPANYCODE = DIRECTIVETEMPLATE.COMPANYCODE AND DIRECTIVETEMPLATEINPUTFIELD.DIRECTIVETEMPLATECODE = DIRECTIVETEMPLATE.CODE` |
| `DIRECTIVETEMPLATE_OUTPUTFIELD` | [`DIRECTIVETEMPLATEOUTPUTFIELD`](../ITEM_MASTER/DIRECTIVETEMPLATEOUTPUTFIELD.md) | `DIRECTIVETEMPLATECOMPANYCODE`, `DIRECTIVETEMPLATECODE` | `DIRECTIVETEMPLATEOUTPUTFIELD.DIRECTIVETEMPLATECOMPANYCODE = DIRECTIVETEMPLATE.COMPANYCODE AND DIRECTIVETEMPLATEOUTPUTFIELD.DIRECTIVETEMPLATECODE = DIRECTIVETEMPLATE.CODE` |

## Indexes

- `DIRECTIVETEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ACTIVE,
       t.RUNBEFORESTANDARDRULES,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.DIRECTIVETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
