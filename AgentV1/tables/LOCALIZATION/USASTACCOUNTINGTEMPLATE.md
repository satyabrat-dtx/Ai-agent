# DB2ADMIN.USASTACCOUNTINGTEMPLATE

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `TEMPLATECODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108006

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TEMPLATECODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ONITEMTYPE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ITEMMANAGEMENT` | CHAR(1) |  |  |  |  |
| 7 | `ONLOGICALWAREHOUSE` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ONARTICLEGROUP` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ONQUALITYLEVEL` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ONORDERTEMPLATE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ONPARTNER` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `ONCOSTCENTER` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ONCOSTCENTERGROUP` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USASTACCOUNTINGTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `USASTACCOUNTINGTEMPLATE_ACCOUNTINGTEMPLATE` | [`USASTACCOUNTINGDEFINITION`](../LOCALIZATION/USASTACCOUNTINGDEFINITION.md) | `COMPANYCODE`, `ACCOUNTINGTEMPLATETEMPLATECODE` | `USASTACCOUNTINGDEFINITION.COMPANYCODE = USASTACCOUNTINGTEMPLATE.COMPANYCODE AND USASTACCOUNTINGDEFINITION.ACCOUNTINGTEMPLATETEMPLATECODE = USASTACCOUNTINGTEMPLATE.TEMPLATECODE` |

## Indexes

- `USASTACCOUNTINGTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TEMPLATECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ONITEMTYPE,
       t.ITEMMANAGEMENT,
       t.ONLOGICALWAREHOUSE,
       t.ONARTICLEGROUP,
       t.ONQUALITYLEVEL,
       t.ONORDERTEMPLATE,
       t.ONPARTNER
FROM   DB2ADMIN.USASTACCOUNTINGTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
