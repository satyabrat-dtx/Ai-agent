# DB2ADMIN.LOGQUALITYHEADER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 66
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 212047

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(20) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `SUBGROUPCODE` | CHAR(5) | NOT NULL |  |  |  |
| 3 | `NUMBERID` | INTEGER | NOT NULL |  |  |  |
| 4 | `STATUSINACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `DETAILREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `TEMPLATECODE` | CHAR(5) |  |  |  |  |
| 11 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 12 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 13 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 14 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `QAITEMGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `QAITEMGROUPCODE` | CHAR(10) |  |  |  |  |
| 25 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 27 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 28 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 29 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 30 | `ADNAMEFORTESTRESULT` | CHAR(50) |  |  |  |  |
| 31 | `QASTATUSCODE` | CHAR(20) |  |  |  |  |
| 32 | `NRTEST` | INTEGER | NOT NULL |  |  |  |
| 33 | `NROFRETRYIFFAILED` | INTEGER | NOT NULL |  |  |  |
| 34 | `RETRYONLYFORFAILEDLINES` | SMALLINT | NOT NULL |  |  |  |
| 35 | `SAMPLE` | SMALLINT | NOT NULL |  |  |  |
| 36 | `SAMPLEINSTRUCTIONCODE` | CHAR(3) |  |  |  |  |
| 37 | `SAMPLELENGTH` | DECIMAL(10,5) |  |  |  |  |
| 38 | `PRECREATEREPETITIONLINES` | SMALLINT | NOT NULL |  |  |  |
| 39 | `CALLQCVERIFY` | SMALLINT | NOT NULL |  |  |  |
| 40 | `QCVERIFY` | CHAR(1) |  |  |  |  |
| 41 | `FREQUENCYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 42 | `FREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 43 | `QUANTITYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 44 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 45 | `OCCURRENCESCHECK` | SMALLINT | NOT NULL |  |  |  |
| 46 | `OCCURRENCES` | INTEGER | NOT NULL |  |  |  |
| 47 | `LASTAUTOMATICDOCDATE` | DATE |  |  |  |  |
| 48 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 49 | `ENTITYKEYVECTOR` | VARCHAR(2000) |  |  |  |  |
| 50 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 51 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 52 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 53 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 54 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 55 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 56 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 57 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 58 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 59 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 60 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 61 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 62 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 63 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 64 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 65 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGQUALITYHEADER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.SUBGROUPCODE,
       t.NUMBERID,
       t.STATUSINACTIVE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DETAILREQUIRED,
       t.ORDERPARTNERREQUIRED,
       t.TEMPLATECODE,
       t.ITEMTYPEAFICOMPANYCODE
FROM   DB2ADMIN.LOGQUALITYHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
