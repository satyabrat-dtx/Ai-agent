# DB2ADMIN.APPROVALREQUESTTEMPLATE

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206477

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `APPROVALREQUESTTYPE` | INTEGER | NOT NULL |  |  |  |
| 8 | `APPROVALREQUESTIDENTIFIER` | CHAR(90) | NOT NULL |  |  |  |
| 9 | `EXPECTEDORDER` | SMALLINT | NOT NULL |  |  |  |
| 10 | `QUALITYTESTREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `COUNTERREQUESTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `COUNTERREQUESTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 13 | `CHANGEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 14 | `VALIDATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 15 | `STATUSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 16 | `SHIPMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 17 | `TNAHEADERCODE` | CHAR(10) |  | FK | foreign_key |  |
| 18 | `LOGMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `REASONHEADERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 20 | `REASONROWSREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 21 | `UGGFORREAREQUIREDCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `UGGFORREASONREQUIREDCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `BLOCKENTITYLINKED` | SMALLINT | NOT NULL |  |  |  |
| 24 | `BLOCKREASONORDERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 25 | `BLOCKREASONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 31 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BLOCKS_BLOCKREASON` | `COMPANYCODE`, `BLOCKREASONORDERTYPE`, `BLOCKREASONCODE` | [`BLOCKS`](../CORE_MASTER/BLOCKS.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `APPROVALREQUESTTEMPLATE.COMPANYCODE = BLOCKS.COMPANYCODE AND APPROVALREQUESTTEMPLATE.BLOCKREASONORDERTYPE = BLOCKS.ORDERTYPE AND APPROVALREQUESTTEMPLATE.BLOCKREASONCODE = BLOCKS.CODE` |
| `COUNTER_COUNTERREQUEST` | `COUNTERREQUESTCOMPANYCODE`, `COUNTERREQUESTCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPROVALREQUESTTEMPLATE.COUNTERREQUESTCOMPANYCODE = COUNTER.COMPANYCODE AND APPROVALREQUESTTEMPLATE.COUNTERREQUESTCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPROVALREQUESTTEMPLATE.COMPANYCODE = DIVISION.COMPANYCODE AND APPROVALREQUESTTEMPLATE.DIVISIONCODE = DIVISION.CODE` |
| `TNAHEADER_TNAHEADER` | `COMPANYCODE`, `TNAHEADERCODE` | [`TNAHEADER`](../TNA/TNAHEADER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPROVALREQUESTTEMPLATE.COMPANYCODE = TNAHEADER.COMPANYCODE AND APPROVALREQUESTTEMPLATE.TNAHEADERCODE = TNAHEADER.CODE` |
| `USERGENERICGROUPTYPE_UGGFORREASONREQUIRED` | `UGGFORREAREQUIREDCOMPANYCODE`, `UGGFORREASONREQUIREDCODE` | [`USERGENERICGROUPTYPE`](../CORE_MASTER/USERGENERICGROUPTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPROVALREQUESTTEMPLATE.UGGFORREAREQUIREDCOMPANYCODE = USERGENERICGROUPTYPE.COMPANYCODE AND APPROVALREQUESTTEMPLATE.UGGFORREASONREQUIREDCODE = USERGENERICGROUPTYPE.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `APPROVALREQUESTTEMPLATE_TEMPLATE` | [`APPROVALREQUEST`](../CORE_MASTER/APPROVALREQUEST.md) | `COMPANYCODE`, `TEMPLATECODE` | `APPROVALREQUEST.COMPANYCODE = APPROVALREQUESTTEMPLATE.COMPANYCODE AND APPROVALREQUEST.TEMPLATECODE = APPROVALREQUESTTEMPLATE.CODE` |
| `APPROVALREQUESTTEMPLATE_ARTEMPLATE` | [`DEVELOPMENTREQUESTTEMPLATE`](../SALES/DEVELOPMENTREQUESTTEMPLATE.md) | `COMPANYCODE`, `ARTEMPLATECODE` | `DEVELOPMENTREQUESTTEMPLATE.COMPANYCODE = APPROVALREQUESTTEMPLATE.COMPANYCODE AND DEVELOPMENTREQUESTTEMPLATE.ARTEMPLATECODE = APPROVALREQUESTTEMPLATE.CODE` |

## Indexes

- `APPROVALREQUESTTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.APPROVALREQUESTTYPE,
       t.APPROVALREQUESTIDENTIFIER,
       t.EXPECTEDORDER,
       t.QUALITYTESTREQUIRED,
       t.COUNTERREQUESTCOMPANYCODE
FROM   DB2ADMIN.APPROVALREQUESTTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
