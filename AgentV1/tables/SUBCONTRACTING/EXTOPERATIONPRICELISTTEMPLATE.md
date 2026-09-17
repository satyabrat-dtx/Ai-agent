# DB2ADMIN.EXTOPERATIONPRICELISTTEMPLATE

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOPERATION')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `DEFINITIONTYPE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 39527

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DEFINITIONTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ORDERCATEGORYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `STATISTICALGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERTEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `PAYMENTMETHODREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `ORDERITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `ENTRYITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `QUALITYLEVELREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `COMMENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 15 | `COMMENTCHOOSEKEYSORDERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 16 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 17 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMMENTCHOOSEKEYSHEADER_COMMENTCHOOSEKEYS` | `COMPANYCODE`, `COMMENTCHOOSEKEYSORDERTYPE`, `COMMENTCHOOSEKEYSTYPE`, `COMMENTCHOOSEKEYSCODE` | [`COMMENTCHOOSEKEYSHEADER`](../CORE_MASTER/COMMENTCHOOSEKEYSHEADER.md) | `COMPANYCODE`, `ORDERTYPE`, `TYPE`, `CODE` | RESTRICT | `EXTOPERATIONPRICELISTTEMPLATE.COMPANYCODE = COMMENTCHOOSEKEYSHEADER.COMPANYCODE AND EXTOPERATIONPRICELISTTEMPLATE.COMMENTCHOOSEKEYSORDERTYPE = COMMENTCHOOSEKEYSHEADER.ORDERTYPE AND EXTOPERATIONPRICELISTTEMPLATE.COMMENTCHOOSEKEYSTYPE = COMMENTCHOOSEKEYSHEADER.TYPE AND EXTOPERATIONPRICELISTTEMPLATE.COMMENTCHOOSEKEYSCODE = COMMENTCHOOSEKEYSHEADER.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EXTOPERATIONPRICELISTTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EXTOPERATIONPRICELISTTEMPLATE_TEMPLATE` | [`EXTOPPRICE`](../SUBCONTRACTING/EXTOPPRICE.md) | `EXTOPPRICELISTCOMPANYCODE`, `TEMPLATEDEFINITIONTYPE`, `TEMPLATECODE` | `EXTOPPRICE.EXTOPPRICELISTCOMPANYCODE = EXTOPERATIONPRICELISTTEMPLATE.COMPANYCODE AND EXTOPPRICE.TEMPLATEDEFINITIONTYPE = EXTOPERATIONPRICELISTTEMPLATE.DEFINITIONTYPE AND EXTOPPRICE.TEMPLATECODE = EXTOPERATIONPRICELISTTEMPLATE.CODE` |
| `EXTOPERATIONPRICELISTTEMPLATE_TEMPLATE` | [`EXTOPPRICELIST`](../SUBCONTRACTING/EXTOPPRICELIST.md) | `COMPANYCODE`, `TEMPLATEDEFINITIONTYPE`, `TEMPLATECODE` | `EXTOPPRICELIST.COMPANYCODE = EXTOPERATIONPRICELISTTEMPLATE.COMPANYCODE AND EXTOPPRICELIST.TEMPLATEDEFINITIONTYPE = EXTOPERATIONPRICELISTTEMPLATE.DEFINITIONTYPE AND EXTOPPRICELIST.TEMPLATECODE = EXTOPERATIONPRICELISTTEMPLATE.CODE` |

## Indexes

- `EXTOPERATIONPRCLISTTMPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DEFINITIONTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ORDERCATEGORYREQUIRED,
       t.STATISTICALGROUPREQUIRED,
       t.ORDERTEMPLATECODEREQUIRED,
       t.PAYMENTMETHODREQUIRED,
       t.ORDERITEMREQUIRED,
       t.ENTRYITEMREQUIRED
FROM   DB2ADMIN.EXTOPERATIONPRICELISTTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
