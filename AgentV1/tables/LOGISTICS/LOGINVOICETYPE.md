# DB2ADMIN.LOGINVOICETYPE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 79
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218324

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `INVOICECATEGORYCODE` | CHAR(3) |  |  |  |  |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `EFFECTIVEFROMDATE` | DATE | NOT NULL |  |  |  |
| 8 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 9 | `NUMBERING` | INTEGER | NOT NULL |  |  |  |
| 10 | `INVOICEPREFIXCODE` | CHAR(8) |  |  |  |  |
| 11 | `CATEGORYOFINVOICE` | INTEGER | NOT NULL |  |  |  |
| 12 | `TYPEOFINVOICE` | INTEGER | NOT NULL |  |  |  |
| 13 | `FROMEQBCODE` | VARCHAR(100) |  |  |  |  |
| 14 | `SALESINTERFACELEVEL` | INTEGER | NOT NULL |  |  |  |
| 15 | `PRESHIPMENTINVREQD` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CUSTOMDISCOUNT` | SMALLINT | NOT NULL |  |  |  |
| 17 | `DUTYPAID` | INTEGER | NOT NULL |  |  |  |
| 18 | `SMSALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 19 | `INVOICECURRENCY` | INTEGER | NOT NULL |  |  |  |
| 20 | `FLAGFROMINVOICECATEGORY` | INTEGER | NOT NULL |  |  |  |
| 21 | `DEFAULTDLVTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `DEFAULTDELIVERYTERMSCODE` | CHAR(3) |  |  |  |  |
| 23 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 24 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 25 | `MULTIPLECHAPTERID` | SMALLINT | NOT NULL |  |  |  |
| 26 | `CONTAINERCALLCODE` | CHAR(1) | NOT NULL |  |  |  |
| 27 | `UPDATEEXC` | SMALLINT | NOT NULL |  |  |  |
| 28 | `RETRIEVEEXC` | SMALLINT | NOT NULL |  |  |  |
| 29 | `POSTINGFLAG` | SMALLINT | NOT NULL |  |  |  |
| 30 | `FLAGMULTIPLESOURCE` | INTEGER | NOT NULL |  |  |  |
| 31 | `FIRMCODE` | CHAR(3) |  |  |  |  |
| 32 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 33 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 34 | `ALCODE` | CHAR(30) |  |  |  |  |
| 35 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 36 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 37 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 38 | `NUMBEROFBALETYPE` | CHAR(2) |  |  |  |  |
| 39 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 41 | `IPPOLICYNO` | CHAR(30) |  |  |  |  |
| 42 | `IPPOLICYDATE` | DATE |  |  |  |  |
| 43 | `POLICYEXPIRYDATE` | DATE |  |  |  |  |
| 44 | `INSURANCECOMPANY` | VARCHAR(140) |  |  |  |  |
| 45 | `INSURANCEMARKUP` | DECIMAL(9,5) |  |  |  |  |
| 46 | `DEFAULTCOMMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 47 | `DEFAULTCOMMENTORDERTYPE` | CHAR(1) |  |  |  |  |
| 48 | `DEFAULTCOMMENTCODE` | CHAR(12) |  |  |  |  |
| 49 | `DEFAULTMESSAGE` | VARCHAR(140) |  |  |  |  |
| 50 | `DEFAULTTAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 51 | `DEFAULTTAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 52 | `COUNTRYOFORIGINOFGOODSCODE` | CHAR(3) |  |  |  |  |
| 53 | `FLAGLCLFCL` | INTEGER | NOT NULL |  |  |  |
| 54 | `CLEARAGAINST` | CHAR(25) |  |  |  |  |
| 55 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 56 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 57 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 58 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 59 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 60 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 61 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 62 | `NOTIFICATIONDETAIL1` | CHAR(120) |  |  |  |  |
| 63 | `NOTIFICATIONDETAIL2` | CHAR(120) |  |  |  |  |
| 64 | `ASSETSPOSTINGFLAG` | SMALLINT | NOT NULL |  |  |  |
| 65 | `MASSPOSTINGFLAG` | SMALLINT | NOT NULL |  |  |  |
| 66 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 67 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 68 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 69 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 70 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 71 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 72 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 73 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 74 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 75 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 76 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 77 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 78 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGINVOICETYPE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGINVOICETYPEDETAIL`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.INVOICECATEGORYCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.NUMBERING,
       t.INVOICEPREFIXCODE,
       t.CATEGORYOFINVOICE
FROM   DB2ADMIN.LOGINVOICETYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
