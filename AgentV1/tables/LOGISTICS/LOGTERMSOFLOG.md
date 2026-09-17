# DB2ADMIN.LOGTERMSOFLOG

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 101
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 208646

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `CODE` | CHAR(2) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `UPDATEREASONREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `VALID` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SALESORDERLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 9 | `SALESORDERCOMMISSIONLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 10 | `SALESORDERLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 11 | `SALESORDERDISCOUNTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 12 | `SALESORDERBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 13 | `SALESORDERCHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 14 | `SALESORDERASSORTMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 15 | `SALESORDERDELIVERYLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 16 | `SALORDDLVBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 17 | `SALORDLINEDISCOUNTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 18 | `SALESORDERLINECOMMLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 19 | `SALESORDERLINEBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 20 | `SALESORDERLINECHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 21 | `SALESCLAIMLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 22 | `SALCLAIMLINEDSCLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 23 | `SALESORDERLINEPRICELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 24 | `PURCHASEORDERLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 25 | `PURCHASEORDERLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 26 | `PURORDERASSORTMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 27 | `PURCHASEORDERBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 28 | `PURCHASEORDERCHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 29 | `PURORDERDISCOUNTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 30 | `PURORDERDELIVERYLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 31 | `PURORDLINEDISCOUNTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 32 | `PURORDERLINECHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 33 | `PURORDERLINEBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 34 | `PURORDDLVBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 35 | `PURRETURNDOCUMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 36 | `SALESDOCUMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 37 | `SALESDOCUMENTLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 38 | `SALDOCUMENTDISCOUNTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 39 | `SALESDOCUMENTCHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 40 | `SALESDOCUMENTBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 41 | `SALDOCLINEDISCOUNTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 42 | `SALDOCLINECHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 43 | `SALDOCUMENTLINECOMMLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 44 | `SALDOCLINEBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 45 | `SALDOCCOMMISSIONLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 46 | `SALESRELEASELINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 47 | `SALRELEASELINEDSCLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 48 | `SALESRELEASELINECOMMLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 49 | `SALRELEASELINEBLKLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 50 | `SALRELEASELINECHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 51 | `INTERNALORDERLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 52 | `INTERNALORDERLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 53 | `INTERNALORDERBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 54 | `INTORDERASSORTMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 55 | `INTORDERDELIVERYLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 56 | `INTORDDLVBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 57 | `INTORDERLINEBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 58 | `INTERNALDOCUMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 59 | `INTERNALDOCUMENTLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 60 | `INTDOCUMENTBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 61 | `INTDOCLINEBLOCKSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 62 | `INTRETURNDOCUMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 63 | `PRODUCTIONDEMANDLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 64 | `EXTOPLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 65 | `EXTOPLINERESERVATIONLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 66 | `EXTOPLINESTOCKTRNLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 67 | `EXTOPLINESUPWHSTRNLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 68 | `EXTOPLINEENTRYTRNLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 69 | `EXTOPLINEPROPROGRESSLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 70 | `EXTOPLINECOMMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 71 | `EXTOPLINEDISCOUNTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 72 | `EXTOPLINECHARGELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 73 | `MSEEXTOPLINEINFOLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 74 | `MSEEXTOPLINECHECKLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 75 | `EXTOPDOCUMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 76 | `EXTOPDOCUMENTLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 77 | `EXTOPDOCLINEISSUETRNLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 78 | `EXTOPDOCLINEENTRYTRNLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 79 | `EXTOPDOCUMENTCOMMENTLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 80 | `EXTOPDOCLINEPRODPRGLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 81 | `QAHEADERLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 82 | `QALINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 83 | `QADOCUMENTHEADERLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 84 | `QADOCUMENTLINELOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 85 | `TESTLOGLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 86 | `TESTLOGCLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 87 | `TESTLOGGCLOGOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 88 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 89 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 90 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 91 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 92 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 93 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 94 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 95 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 96 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 97 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 98 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 99 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 100 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGTERMSOFLOG.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.UPDATEREASONREQUIRED,
       t.VALID,
       t.SALESORDERLOGOPTIONS,
       t.SALESORDERCOMMISSIONLOGOPTIONS,
       t.SALESORDERLINELOGOPTIONS,
       t.SALESORDERDISCOUNTLOGOPTIONS
FROM   DB2ADMIN.LOGTERMSOFLOG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
