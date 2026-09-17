# DB2ADMIN.TAXDEFINITIONTEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `DEFINITIONTYPE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 1955

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `DEFINITIONTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `ORDERCATEGORYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `ORDERTEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `ORDERITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `ORDERITEMGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `ORDERLINETEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `LINEUSERVALUEREQUIRED` | CHAR(1) |  |  |  |  |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `REFERENCEPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 24 | `REFERENCEPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TAXDEFINITIONTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TAXDEFINITIONTEMPLATE_TEMPLATE` | [`SALESTAXDEFINITION`](../SALES/SALESTAXDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TAXTYPE`, `TEMPLATECODE` | `SALESTAXDEFINITION.COMPANYCODE = TAXDEFINITIONTEMPLATE.COMPANYCODE AND SALESTAXDEFINITION.ORDERTYPE = TAXDEFINITIONTEMPLATE.ORDERTYPE AND SALESTAXDEFINITION.TAXTYPE = TAXDEFINITIONTEMPLATE.DEFINITIONTYPE AND SALESTAXDEFINITION.TEMPLATECODE = TAXDEFINITIONTEMPLATE.CODE` |
| `TAXDEFINITIONTEMPLATE_TEMPLATE` | [`PURCHASETAXDEFINITION`](../PURCHASING/PURCHASETAXDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TAXTYPE`, `TEMPLATECODE` | `PURCHASETAXDEFINITION.COMPANYCODE = TAXDEFINITIONTEMPLATE.COMPANYCODE AND PURCHASETAXDEFINITION.ORDERTYPE = TAXDEFINITIONTEMPLATE.ORDERTYPE AND PURCHASETAXDEFINITION.TAXTYPE = TAXDEFINITIONTEMPLATE.DEFINITIONTYPE AND PURCHASETAXDEFINITION.TEMPLATECODE = TAXDEFINITIONTEMPLATE.CODE` |
| `TAXDEFINITIONTEMPLATE_TEMPLATE` | [`EXTOPERATIONTAXDEFINITION`](../SUBCONTRACTING/EXTOPERATIONTAXDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TAXTYPE`, `TEMPLATECODE` | `EXTOPERATIONTAXDEFINITION.COMPANYCODE = TAXDEFINITIONTEMPLATE.COMPANYCODE AND EXTOPERATIONTAXDEFINITION.ORDERTYPE = TAXDEFINITIONTEMPLATE.ORDERTYPE AND EXTOPERATIONTAXDEFINITION.TAXTYPE = TAXDEFINITIONTEMPLATE.DEFINITIONTYPE AND EXTOPERATIONTAXDEFINITION.TEMPLATECODE = TAXDEFINITIONTEMPLATE.CODE` |

## Indexes

- `TAXDEFINITIONTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.DEFINITIONTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ORDERPARTNERREQUIRED,
       t.ORDERPARTNERGROUPREQUIRED,
       t.ORDERCATEGORYREQUIRED,
       t.ORDERTEMPLATECODEREQUIRED,
       t.ITEMTYPEREQUIRED
FROM   DB2ADMIN.TAXDEFINITIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
